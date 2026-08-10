from __future__ import annotations

import ast
import copy
import json
import math
import re
import sys
import tempfile
import unittest
import unicodedata
import warnings
from pathlib import Path
from unittest import mock


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from ufuq_astronomy_reference import (  # noqa: E402
    BATCH_SPECS,
    ProtocolValidationError,
    run_batch01,
    validate_batch01_artifacts,
)
from ufuq_astronomy_reference import batch01  # noqa: E402
from ufuq_astronomy_reference.experiment_protocol import (  # noqa: E402
    JSON_SCHEMA_DIALECT,
    SUPPORTED_SCHEMA_KEYWORDS,
    canonical_experiment_bytes,
    read_json_strict,
    sha256_bytes,
    validate_instance,
    validate_schema_contract,
)


def decode_result(value: bytes) -> dict:
    result = json.loads(value)
    if not isinstance(result, dict):
        raise AssertionError("Batch result must be an object")
    return result


EPOCH_LOCATION_EXPERIMENT_IDS = (
    "2C.1-EXP-01",
    "2C.1-EXP-02",
    "2C.1-EXP-03",
)


class Batch01ProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.outputs = run_batch01(write_results=False)
        cls.results = {
            spec.experiment_id: decode_result(cls.outputs[spec.result_filename])
            for spec in BATCH_SPECS
        }

    def test_allowlist_rejects_unknown_and_non_batch_registered_ids(self) -> None:
        for rejected in ("UNKNOWN", "2C.2-EXP-03", "2C.2-EXP-05"):
            with self.subTest(rejected=rejected):
                with self.assertRaises(ProtocolValidationError):
                    run_batch01(
                        experiment_ids=[rejected], write_results=False
                    )
        with self.assertRaises(ProtocolValidationError):
            run_batch01(
                experiment_ids=["2C.1-EXP-01", "2C.1-EXP-01"],
                write_results=False,
            )
        with self.assertRaises(ProtocolValidationError):
            run_batch01(experiment_ids=[], write_results=False)
        with self.assertRaises(ProtocolValidationError):
            run_batch01(
                experiment_ids=["2C.1-EXP-01"], write_results=True
            )

    def test_schema_subset_and_all_instances_validate_offline(self) -> None:
        schemas = batch01._schema_bundle()
        registry = read_json_strict(batch01.REGISTRY_PATH)
        validate_instance(registry, schemas["registry"])
        for spec in BATCH_SPECS:
            fixture = read_json_strict(
                batch01.FIXTURE_ROOT / spec.fixture_filename,
                require_canonical=True,
            )
            validate_instance(fixture, schemas["fixture"])
            validate_instance(self.results[spec.experiment_id], schemas["result"])

        invalid_schema = copy.deepcopy(schemas["fixture"])
        invalid_schema["unapprovedKeyword"] = True
        with self.assertRaises(ProtocolValidationError):
            validate_schema_contract(invalid_schema)

        invalid_fixture = copy.deepcopy(
            read_json_strict(
                batch01.FIXTURE_ROOT / BATCH_SPECS[0].fixture_filename,
                require_canonical=True,
            )
        )
        invalid_fixture["unexpected"] = True
        with self.assertRaises(ProtocolValidationError):
            validate_instance(invalid_fixture, schemas["fixture"])

        conditional_fixture = copy.deepcopy(
            read_json_strict(
                batch01.FIXTURE_ROOT
                / batch01.SPEC_BY_ID["2C.4-EXP-06"].fixture_filename,
                require_canonical=True,
            )
        )
        conditional_fixture["inputs"]["missingMeteorology"]["value"] = "PRESENT"
        with self.assertRaises(ProtocolValidationError):
            validate_instance(conditional_fixture, schemas["fixture"])

        nonfinite_fixture = copy.deepcopy(invalid_fixture)
        nonfinite_fixture["inputs"]["declinationDeg"]["value"] = math.inf
        with self.assertRaises(ProtocolValidationError):
            validate_instance(nonfinite_fixture, schemas["fixture"])

        nonlocal_reference = copy.deepcopy(schemas["fixture"])
        nonlocal_reference["properties"]["fixtureId"] = {
            "$ref": "https://example.invalid/schema.json"
        }
        with self.assertRaises(ProtocolValidationError):
            validate_schema_contract(nonlocal_reference)
        del invalid_fixture["unexpected"]
        del invalid_fixture["inputs"]["declinationDeg"]["value"]
        with self.assertRaises(ProtocolValidationError):
            validate_instance(invalid_fixture, schemas["fixture"])

        numerical_result = next(
            result for result in self.results.values() if result["measurements"]
        )
        invalid_result = copy.deepcopy(numerical_result)
        invalid_result["measurements"][0]["acceptanceStatus"] = "PASS"
        with self.assertRaises(ProtocolValidationError):
            validate_instance(invalid_result, schemas["result"])

        epoch_fixture = read_json_strict(
            batch01.FIXTURE_ROOT
            / batch01.SPEC_BY_ID["2C.1-EXP-01"].fixture_filename,
            require_canonical=True,
        )
        missing_geocentre = copy.deepcopy(epoch_fixture)
        del missing_geocentre["inputs"][
            "tdbConversionLocationGeocentricMetres"
        ]
        with self.assertRaises(ProtocolValidationError):
            validate_instance(missing_geocentre, schemas["fixture"])

        nonzero_geocentre = copy.deepcopy(epoch_fixture)
        nonzero_geocentre["inputs"][
            "tdbConversionLocationGeocentricMetres"
        ]["value"] = [1, 0, 0]
        with self.assertRaises(ProtocolValidationError):
            validate_instance(nonzero_geocentre, schemas["fixture"])

        implicit_location = copy.deepcopy(epoch_fixture)
        implicit_location["requiredArtifactStates"]["observer"] = {
            "references": [],
            "requirement": "NOT_REQUIRED",
        }
        with self.assertRaises(ProtocolValidationError):
            validate_instance(implicit_location, schemas["fixture"])

        implicit_leap_state = copy.deepcopy(epoch_fixture)
        implicit_leap_state["requiredArtifactStates"]["leapSeconds"] = {
            "references": [],
            "requirement": "NOT_REQUIRED",
        }
        with self.assertRaises(ProtocolValidationError):
            validate_instance(implicit_leap_state, schemas["fixture"])

        undisclosed_artifact = copy.deepcopy(registry)
        next(
            record
            for record in undisclosed_artifact["experiments"]
            if record["experimentId"] == "2C.1-EXP-01"
        )["inputClasses"] = ["SYNTHETIC"]
        with self.assertRaises(ProtocolValidationError):
            batch01.validate_registry(
                undisclosed_artifact, schemas["registry"]
            )

    def test_schema_contract_matches_exact_used_keyword_subset(self) -> None:
        used_keywords: set[str] = set()

        def walk(node: object) -> None:
            if not isinstance(node, dict):
                return
            used_keywords.update(node)
            for collection_name in ("$defs", "properties"):
                collection = node.get(collection_name, {})
                if isinstance(collection, dict):
                    for child in collection.values():
                        walk(child)
            for collection_name in ("allOf", "oneOf", "prefixItems"):
                collection = node.get(collection_name, [])
                if isinstance(collection, list):
                    for child in collection:
                        walk(child)
            for name in (
                "additionalProperties",
                "contains",
                "else",
                "if",
                "items",
                "not",
                "propertyNames",
                "then",
            ):
                walk(node.get(name))

        for schema in batch01._schema_bundle().values():
            walk(schema)
        self.assertEqual(used_keywords, SUPPORTED_SCHEMA_KEYWORDS)

    def test_schema_contract_rejects_unsupported_keyword_value_shapes(self) -> None:
        def schema_with(name: str, value: object) -> dict:
            return {
                "$id": "urn:ufuq:test:local-schema-subset",
                "$schema": JSON_SCHEMA_DIALECT,
                "type": "string",
                name: value,
            }

        invalid_keyword_values = {
            "$defs-not-object": ("$defs", []),
            "$defs-child-not-schema": ("$defs", {"value": True}),
            "$id-not-string": ("$id", 1),
            "$ref-not-string": ("$ref", 1),
            "$schema-not-string": ("$schema", 1),
            "$schema-wrong-dialect": ("$schema", "draft-unknown"),
            "additionalProperties-not-schema": ("additionalProperties", []),
            "allOf-empty": ("allOf", []),
            "allOf-not-array": ("allOf", {}),
            "allOf-child-not-schema": ("allOf", [True]),
            "const-not-canonical": ("const", math.inf),
            "contains-not-schema": ("contains", True),
            "description-not-string": ("description", 1),
            "else-not-schema": ("else", True),
            "enum-empty": ("enum", []),
            "enum-not-array": ("enum", "VALUE"),
            "enum-duplicate": ("enum", ["VALUE", "VALUE"]),
            "if-not-schema": ("if", True),
            "items-not-schema": ("items", []),
            "maxItems-bool": ("maxItems", True),
            "maxItems-negative": ("maxItems", -1),
            "minItems-not-integer": ("minItems", "1"),
            "minLength-negative": ("minLength", -1),
            "minProperties-bool": ("minProperties", False),
            "minimum-bool": ("minimum", True),
            "minimum-not-finite": ("minimum", math.inf),
            "not-not-schema": ("not", True),
            "oneOf-empty": ("oneOf", []),
            "oneOf-not-array": ("oneOf", {}),
            "pattern-invalid": ("pattern", "["),
            "prefixItems-empty": ("prefixItems", []),
            "prefixItems-not-array": ("prefixItems", {}),
            "properties-not-object": ("properties", []),
            "properties-child-not-schema": ("properties", {"value": True}),
            "propertyNames-not-schema": ("propertyNames", True),
            "required-not-array": ("required", "value"),
            "required-duplicate": ("required", ["value", "value"]),
            "then-not-schema": ("then", True),
            "title-not-string": ("title", 1),
            "type-array-not-supported": ("type", ["string"]),
            "type-name-not-supported": ("type", "date"),
            "uniqueItems-not-boolean": ("uniqueItems", "true"),
        }
        for case_name, (keyword, value) in invalid_keyword_values.items():
            with self.subTest(case_name=case_name):
                with self.assertRaises(ProtocolValidationError):
                    validate_schema_contract(schema_with(keyword, value))

        for scoped_keyword, value in (
            ("$defs", {"value": {"type": "string"}}),
            ("$id", "urn:ufuq:test:nested"),
            ("$schema", JSON_SCHEMA_DIALECT),
        ):
            with self.subTest(scoped_keyword=scoped_keyword):
                schema = schema_with(
                    "properties", {"value": {scoped_keyword: value}}
                )
                schema["type"] = "object"
                with self.assertRaises(ProtocolValidationError):
                    validate_schema_contract(schema)

        for reference in (
            "https://example.invalid/schema.json",
            "#/$defs/missing",
        ):
            with self.subTest(reference=reference):
                with self.assertRaises(ProtocolValidationError):
                    validate_schema_contract(schema_with("$ref", reference))

    def test_each_supported_instance_constraint_has_a_negative_case(self) -> None:
        def assert_rejected(
            case_name: str, instance: object, schema_body: dict
        ) -> None:
            schema = {
                "$id": f"urn:ufuq:test:{case_name}",
                "$schema": JSON_SCHEMA_DIALECT,
                **schema_body,
            }
            validate_schema_contract(schema)
            with self.subTest(case_name=case_name):
                with self.assertRaises(ProtocolValidationError):
                    validate_instance(instance, schema)

        type_cases = {
            "array": {},
            "boolean": 0,
            "integer": 1.5,
            "null": False,
            "number": "1",
            "object": [],
            "string": 1,
        }
        for expected_type, invalid_instance in type_cases.items():
            assert_rejected(
                f"type-{expected_type}",
                invalid_instance,
                {"type": expected_type},
            )

        negative_cases = {
            "$ref": (
                "NO",
                {
                    "$defs": {"expected": {"const": "YES"}},
                    "$ref": "#/$defs/expected",
                },
            ),
            "additionalProperties-false": (
                {"extra": 1},
                {
                    "additionalProperties": False,
                    "properties": {},
                    "type": "object",
                },
            ),
            "additionalProperties-schema": (
                {"extra": 1},
                {
                    "additionalProperties": {"type": "string"},
                    "properties": {},
                    "type": "object",
                },
            ),
            "allOf": ("x", {"allOf": [{"minLength": 2}], "type": "string"}),
            "const": ("NO", {"const": "YES"}),
            "contains": (["NO"], {"contains": {"const": "YES"}, "type": "array"}),
            "if-then": (
                {"mode": "THEN"},
                {
                    "if": {
                        "properties": {"mode": {"const": "THEN"}},
                        "required": ["mode"],
                    },
                    "properties": {"mode": {"type": "string"}},
                    "then": {"required": ["requiredByThen"]},
                    "type": "object",
                },
            ),
            "if-else": (
                {"mode": "ELSE"},
                {
                    "else": {"required": ["requiredByElse"]},
                    "if": {
                        "properties": {"mode": {"const": "THEN"}},
                        "required": ["mode"],
                    },
                    "properties": {"mode": {"type": "string"}},
                    "type": "object",
                },
            ),
            "enum": ("NO", {"enum": ["YES"]}),
            "items-false": (
                ["first", "extra"],
                {
                    "items": False,
                    "prefixItems": [{"const": "first"}],
                    "type": "array",
                },
            ),
            "items-schema": ([1], {"items": {"type": "string"}, "type": "array"}),
            "maxItems": ([1, 2], {"maxItems": 1, "type": "array"}),
            "minItems": ([], {"minItems": 1, "type": "array"}),
            "minLength": ("x", {"minLength": 2, "type": "string"}),
            "minProperties": ({}, {"minProperties": 1, "type": "object"}),
            "minimum": (-1, {"minimum": 0, "type": "number"}),
            "not": ("NO", {"not": {"const": "NO"}}),
            "oneOf-no-match": (
                "NO",
                {"oneOf": [{"const": "A"}, {"const": "B"}]},
            ),
            "oneOf-multiple-matches": (
                "YES",
                {"oneOf": [{"type": "string"}, {"minLength": 1}]},
            ),
            "pattern": ("lower", {"pattern": "^[A-Z]+$", "type": "string"}),
            "prefixItems": (
                ["NO"],
                {
                    "items": False,
                    "prefixItems": [{"const": "YES"}],
                    "type": "array",
                },
            ),
            "properties": (
                {"value": 1},
                {
                    "properties": {"value": {"type": "string"}},
                    "type": "object",
                },
            ),
            "propertyNames": (
                {"lower": 1},
                {"propertyNames": {"pattern": "^[A-Z]+$"}, "type": "object"},
            ),
            "required": ({}, {"required": ["value"], "type": "object"}),
            "uniqueItems": ([1, 1], {"type": "array", "uniqueItems": True}),
        }
        for case_name, (instance, schema_body) in negative_cases.items():
            assert_rejected(case_name, instance, schema_body)

    def test_fixture_inventory_scope_and_source_prohibitions_are_exact(self) -> None:
        fixture_paths = sorted(batch01.FIXTURE_ROOT.glob("*.json"))
        self.assertEqual(len(fixture_paths), 9)
        self.assertEqual(
            {path.name for path in fixture_paths},
            {spec.fixture_filename for spec in BATCH_SPECS},
        )
        for spec in BATCH_SPECS:
            fixture = read_json_strict(
                batch01.FIXTURE_ROOT / spec.fixture_filename,
                require_canonical=True,
            )
            self.assertEqual(
                fixture["inputClassification"],
                "SYNTHETIC_EXPERIMENT_INPUT",
            )
            self.assertTrue(all(fixture["sourceProhibitions"].values()))
            self.assertEqual(tuple(fixture["parameterPartition"]), spec.partitions)
            self.assertEqual(
                fixture["fixtureId"],
                f"{fixture['experimentId']}:{fixture['caseId']}",
            )
            if spec.experiment_id in EPOCH_LOCATION_EXPERIMENT_IDS:
                location = fixture["inputs"][
                    "tdbConversionLocationGeocentricMetres"
                ]
                self.assertEqual(
                    location,
                    {
                        "coordinateConvention": (
                            "CARTESIAN_XYZ_AT_EARTH_CENTRE"
                        ),
                        "frame": "ITRS_GEOCENTRIC",
                        "inputIntent": "VALID_VALUE",
                        "provenance": "SYNTHETIC_EXPLICIT",
                        "semanticRole": "TDB_MINUS_TT_REFERENCE_LOCATION",
                        "timeScale": "NOT_APPLICABLE",
                        "unit": "METRE",
                        "value": [0, 0, 0],
                    },
                )
                self.assertEqual(
                    fixture["requiredArtifactStates"]["observer"],
                    {
                        "references": [
                            "inputs.tdbConversionLocationGeocentricMetres"
                        ],
                        "requirement": "SYNTHETIC_EXPLICIT",
                    },
                )
                self.assertTrue(spec.uses_leap_seconds)
                self.assertEqual(
                    fixture["requiredArtifactStates"]["leapSeconds"],
                    {
                        "references": [
                            "astropy-iers-data/Leap_Second.dat"
                        ],
                        "requirement": "PINNED_EXTERNAL_SMOKE_ONLY",
                    },
                )
                self.assertEqual(
                    [
                        (record["artifactId"], record["role"])
                        for record in fixture["usedArtifactHashes"]
                    ],
                    [
                        (
                            "astropy-iers-data/Leap_Second.dat",
                            "LEAP_SECONDS",
                        )
                    ],
                )
                self.assertIn(
                    "ITRS_GEOCENTRIC", fixture["conventions"]["frames"]
                )
                self.assertIn("METRE", fixture["conventions"]["units"])
        motion = read_json_strict(
            batch01.FIXTURE_ROOT
            / batch01.SPEC_BY_ID["2C.2-EXP-04"].fixture_filename,
            require_canonical=True,
        )
        self.assertEqual(
            motion["parameterPartition"],
            [
                "OMITTED_COSINE_GUARD",
                "DOUBLE_COSINE_GUARD",
                "DECLARED_TARGET_EPOCH_LABEL_GUARD",
                "TWO_PART_JD_SPLIT_INVARIANT",
                "WARNING_STATUS_PRESERVATION",
            ],
        )

        mutated = copy.deepcopy(motion)
        mutated["inputs"]["rightAscensionRad"]["value"] = "HIP 123"
        with self.assertRaises(ProtocolValidationError):
            batch01._scan_fixture_inputs(mutated)
        mutated = copy.deepcopy(motion)
        mutated["inputs"]["catalogueSourceBytes"] = mutated["inputs"].pop(
            "rightAscensionRad"
        )
        with self.assertRaises(ProtocolValidationError):
            batch01._scan_fixture_inputs(mutated)

        mutated = copy.deepcopy(motion)
        mutated["inputs"]["rightAscensionRad"]["unit"] = "DEGREE"
        with self.assertRaises(ProtocolValidationError):
            batch01.validate_fixture(
                batch01.SPEC_BY_ID["2C.2-EXP-04"],
                mutated,
                canonical_experiment_bytes(mutated),
                batch01._schema_bundle()["fixture"],
                read_json_strict(batch01.REGISTRY_PATH),
            )

    def test_canonicalization_is_strict_and_not_a_correctness_claim(self) -> None:
        value = {"z": 1e20, "a": "e\u0301", "array": [3, 2, 1]}
        canonical = canonical_experiment_bytes(value)
        self.assertTrue(canonical.endswith(b"\n"))
        self.assertFalse(canonical.startswith(b"\xef\xbb\xbf"))
        self.assertNotIn(b"\r", canonical)
        self.assertNotIn(b"e+", canonical)
        decoded = json.loads(canonical)
        self.assertEqual(decoded["a"], unicodedata.normalize("NFC", value["a"]))
        self.assertEqual(decoded["array"], [3, 2, 1])
        with self.assertRaises(ProtocolValidationError):
            canonical_experiment_bytes({"value": -0.0})
        with self.assertRaises(ProtocolValidationError):
            canonical_experiment_bytes({"value": math.inf})
        with self.assertRaises(ProtocolValidationError):
            canonical_experiment_bytes({"value": 2**54})
        with self.assertRaises(ProtocolValidationError):
            canonical_experiment_bytes({"fixtureByteLength": -(2**54)})
        self.assertIn(
            str(2**64).encode("ascii"),
            canonical_experiment_bytes({"fixtureByteLength": 2**64}),
        )
        with self.assertRaises(ProtocolValidationError):
            canonical_experiment_bytes({"é": 1, "e\u0301": 2})

        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            with self.assertRaises(ProtocolValidationError):
                read_json_strict(duplicate)

    def test_two_complete_runs_are_byte_identical(self) -> None:
        second = run_batch01(write_results=False)
        self.assertEqual(self.outputs, second)
        self.assertEqual(
            {name: sha256_bytes(value) for name, value in self.outputs.items()},
            {name: sha256_bytes(value) for name, value in second.items()},
        )

    def test_exact_checks_pass_and_measurements_never_gain_acceptance(self) -> None:
        self.assertEqual(len(self.results), 9)
        exact_pass = 0
        exact_fail = 0
        measurement_only_checks = 0
        measurement_records = 0
        for experiment_id, result in self.results.items():
            self.assertEqual(result["executionOutcome"]["state"], "COMPLETED")
            self.assertEqual(
                result["resultClassification"],
                "SYNTHETIC_EXPERIMENT_EVIDENCE_ONLY",
            )
            self.assertEqual(
                result["errorBudgetStatus"],
                "NOT_ESTABLISHED_AST_006_OPEN",
            )
            for check in result["checks"]:
                if check["kind"] == "EXACT_INVARIANT":
                    self.assertEqual(check["status"], "PASS", experiment_id)
                    exact_pass += check["status"] == "PASS"
                    exact_fail += check["status"] == "FAIL"
                else:
                    self.assertEqual(
                        check["status"],
                        "MEASURED_NO_ACCEPTANCE",
                        experiment_id,
                    )
                    measurement_only_checks += 1
                self.assertIsNone(check["numericalThreshold"])
            for measurement in result["measurements"]:
                self.assertEqual(
                    measurement["acceptanceStatus"],
                    "MEASURED_NO_ACCEPTANCE",
                )
                measurement_records += 1

        self.assertEqual(exact_pass, 24)
        self.assertEqual(exact_fail, 0)
        self.assertEqual(measurement_only_checks, 6)
        self.assertEqual(measurement_records, 27)

    def test_warning_status_and_optional_state_guards_are_preserved(self) -> None:
        for experiment_id in EPOCH_LOCATION_EXPERIMENT_IDS:
            with self.subTest(experiment_id=experiment_id):
                self.assertTrue(
                    any(
                        status["code"]
                        == "SYNTHETIC_GEOCENTRE_LOCATION_EXPLICIT"
                        for status in self.results[experiment_id][
                            "structuredStatuses"
                        ]
                    )
                )

        motion = self.results["2C.2-EXP-04"]
        self.assertTrue(
            any(
                warning["code"] == "ErfaWarning"
                for warning in motion["warnings"]
            )
        )
        self.assertTrue(
            any(
                status["code"] == "PMSAFE_WARNING_STATUS_1"
                for status in motion["structuredStatuses"]
            )
        )

        below = self.results["2C.4-EXP-05"]
        self.assertTrue(
            any(
                status["code"] == "BELOW_GEOMETRIC_HORIZON"
                for status in below["structuredStatuses"]
            )
        )
        refraction = self.results["2C.4-EXP-06"]
        self.assertEqual(
            [status["code"] for status in refraction["structuredStatuses"]],
            ["REFRACTION_NOT_REQUESTED", "REFRACTION_UNAVAILABLE"],
        )
        visibility = self.results["2C.4-EXP-07"]
        self.assertTrue(
            all(check["status"] == "PASS" for check in visibility["checks"])
        )

    def test_epoch_cases_run_alone_with_explicit_location_and_leap_artifact(self) -> None:
        for experiment_id in EPOCH_LOCATION_EXPERIMENT_IDS:
            with self.subTest(experiment_id=experiment_id):
                spec = batch01.SPEC_BY_ID[experiment_id]
                with mock.patch.object(
                    batch01.iers.earth_orientation_table,
                    "get",
                    side_effect=AssertionError(
                        "epoch-label execution must not discover an IERS table"
                    ),
                ):
                    isolated = run_batch01(
                        experiment_ids=[experiment_id], write_results=False
                    )
                self.assertEqual(set(isolated), {spec.result_filename})
                result = decode_result(isolated[spec.result_filename])
                self.assertEqual(
                    [
                        (record["artifactId"], record["role"])
                        for record in result["executionManifest"][
                            "externalArtifactProvenance"
                        ]
                    ],
                    [
                        (
                            "astropy-iers-data/Leap_Second.dat",
                            "LEAP_SECONDS",
                        )
                    ],
                )
                self.assertTrue(
                    any(
                        status["code"]
                        == "SYNTHETIC_GEOCENTRE_LOCATION_EXPLICIT"
                        for status in result["structuredStatuses"]
                    )
                )

    def test_unexpected_outer_warning_is_preserved(self) -> None:
        spec = batch01.SPEC_BY_ID["2C.4-EXP-07"]
        fixture = read_json_strict(
            batch01.FIXTURE_ROOT / spec.fixture_filename,
            require_canonical=True,
        )
        original = batch01.HANDLERS[spec.handler]

        def warning_handler(specification, input_fixture):
            evidence = original(specification, input_fixture)
            warnings.warn("synthetic outer-capture probe", RuntimeWarning)
            return evidence

        batch01.HANDLERS[spec.handler] = warning_handler
        try:
            evidence = batch01._isolated_evidence(spec, fixture)
        finally:
            batch01.HANDLERS[spec.handler] = original
        self.assertTrue(
            any(
                record["code"] == "RuntimeWarning"
                and record["message"] == "synthetic outer-capture probe"
                for record in evidence["warnings"]
            )
        )

    def test_committed_results_hashes_manifests_and_schema_are_current(self) -> None:
        validate_batch01_artifacts()
        self.assertEqual(
            {path.name for path in batch01.RESULT_ROOT.iterdir()},
            {
                name
                for spec in BATCH_SPECS
                for name in (
                    spec.result_filename,
                    Path(spec.result_filename).with_suffix(".sha256").name,
                )
            },
        )
        for spec in BATCH_SPECS:
            result_path = batch01.RESULT_ROOT / spec.result_filename
            result = read_json_strict(result_path, require_canonical=True)
            self.assertEqual(
                result_path.read_bytes(),
                self.outputs[spec.result_filename],
            )
            body = dict(result)
            content_hash = body.pop("canonicalContentSha256")
            self.assertEqual(
                content_hash,
                sha256_bytes(canonical_experiment_bytes(body)),
            )
            companion = result_path.with_suffix(".sha256")
            self.assertEqual(
                companion.read_text(encoding="ascii").strip(),
                sha256_bytes(result_path.read_bytes()),
            )
            manifest = result["executionManifest"]
            self.assertEqual(manifest["repetitionCount"], 2)
            self.assertEqual(
                manifest["networkPolicy"],
                "OFFLINE_AUTO_DOWNLOAD_DISABLED",
            )
            self.assertEqual(
                manifest["cachePolicy"],
                "FRESH_ISOLATED_CACHE_NO_DISCOVERY",
            )
            self.assertEqual(
                manifest["softwareRuntime"]["pyerfaDependencyKind"],
                "DIRECT",
            )
            for source in manifest["runner"]["sourceFiles"]:
                source_path = PROJECT_ROOT / source["path"]
                self.assertEqual(
                    source["sha256"],
                    sha256_bytes(source_path.read_bytes()),
                )

    def test_runner_import_boundary_and_fixture_values_exclude_sources(self) -> None:
        allowed_erfa_import = "src/ufuq_astronomy_reference/batch01.py"
        prohibited_roots = {
            "apps",
            "astronomy_core",
            "assessment_core",
            "catalogue_schema",
            "packages",
            "tutoring_core",
        }
        for source in [PROJECT_ROOT / "run.py", *sorted((PROJECT_ROOT / "src").rglob("*.py"))]:
            tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
            imports = {
                alias.name.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.Import)
                for alias in node.names
            }
            imports.update(
                node.module.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module
            )
            self.assertTrue(imports.isdisjoint(prohibited_roots), str(source))
            relative = source.relative_to(PROJECT_ROOT).as_posix()
            if "erfa" in imports:
                self.assertEqual(relative, allowed_erfa_import)

        runner_tree = ast.parse(
            (PROJECT_ROOT / allowed_erfa_import).read_text(encoding="utf-8")
        )
        function_nodes = {
            node.name: node
            for node in runner_tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        for handler_name in (
            "_experiment_2c1_01",
            "_experiment_2c1_02",
            "_experiment_2c1_03",
        ):
            with self.subTest(handler=handler_name):
                time_calls = [
                    node
                    for node in ast.walk(function_nodes[handler_name])
                    if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "Time"
                ]
                self.assertGreater(len(time_calls), 0)
                self.assertTrue(
                    all(
                        any(keyword.arg == "location" for keyword in call.keywords)
                        for call in time_calls
                    )
                )

        forbidden = re.compile(
            r"(?:I/311|hip2\.dat|hip7p\.dat|hip9p\.dat|hipvim\.dat|\bHIP\s*\d)",
            flags=re.IGNORECASE,
        )
        for spec in BATCH_SPECS:
            fixture = read_json_strict(
                batch01.FIXTURE_ROOT / spec.fixture_filename,
                require_canonical=True,
            )
            self.assertIsNone(forbidden.search(json.dumps(fixture["inputs"])))


if __name__ == "__main__":
    unittest.main()
