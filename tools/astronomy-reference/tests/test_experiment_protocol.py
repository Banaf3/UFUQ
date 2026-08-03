from __future__ import annotations

import ast
import json
import re
import unittest
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
EXPERIMENT_ROOT = PROJECT_ROOT / "experiments"

EXPECTED_CLASSIFICATION_COUNTS = {
    "RUNNABLE_SYNTHETIC_NOW": 17,
    "BLOCKED_BY_SOURCE_AUTHORITY": 0,
    "BLOCKED_BY_PROJECT_DECISION": 5,
    "BLOCKED_BY_REVIEW": 0,
    "BLOCKED_BY_REQUIRED_DATA": 1,
    "DEFERRED_TO_PRODUCTION_IMPLEMENTATION": 1,
}

EXPECTED_EXPERIMENTS = {
    "2C.1-EXP-01": "RUNNABLE_SYNTHETIC_NOW",
    "2C.1-EXP-02": "RUNNABLE_SYNTHETIC_NOW",
    "2C.1-EXP-03": "RUNNABLE_SYNTHETIC_NOW",
    "2C.2-EXP-01": "RUNNABLE_SYNTHETIC_NOW",
    "2C.2-EXP-02": "DEFERRED_TO_PRODUCTION_IMPLEMENTATION",
    "2C.2-EXP-03": "RUNNABLE_SYNTHETIC_NOW",
    "2C.2-EXP-04": "RUNNABLE_SYNTHETIC_NOW",
    "2C.2-EXP-05": "BLOCKED_BY_PROJECT_DECISION",
    "2C.2-EXP-06": "RUNNABLE_SYNTHETIC_NOW",
    "2C.2-EXP-07": "BLOCKED_BY_PROJECT_DECISION",
    "2C.2-EXP-08": "BLOCKED_BY_PROJECT_DECISION",
    "2C.3-EXP-01": "RUNNABLE_SYNTHETIC_NOW",
    "2C.3-EXP-02": "RUNNABLE_SYNTHETIC_NOW",
    "2C.3-EXP-03": "BLOCKED_BY_PROJECT_DECISION",
    "2C.3-EXP-04": "RUNNABLE_SYNTHETIC_NOW",
    "2C.3-EXP-05": "RUNNABLE_SYNTHETIC_NOW",
    "2C.3-EXP-06": "BLOCKED_BY_PROJECT_DECISION",
    "2C.4-EXP-01": "BLOCKED_BY_REQUIRED_DATA",
    "2C.4-EXP-02": "RUNNABLE_SYNTHETIC_NOW",
    "2C.4-EXP-03": "RUNNABLE_SYNTHETIC_NOW",
    "2C.4-EXP-04": "RUNNABLE_SYNTHETIC_NOW",
    "2C.4-EXP-05": "RUNNABLE_SYNTHETIC_NOW",
    "2C.4-EXP-06": "RUNNABLE_SYNTHETIC_NOW",
    "2C.4-EXP-07": "RUNNABLE_SYNTHETIC_NOW",
}

EXPECTED_BATCH = {
    "EPOCH_LABEL_GUARDS": {
        "2C.1-EXP-01": (
            "2C.1-EXP-01-BATCH01-SYNTHETIC",
            ["TT_TDB_UTC_LABEL_SENSITIVITY"],
        ),
        "2C.1-EXP-02": (
            "2C.1-EXP-02-BATCH01-SYNTHETIC",
            ["CALENDAR_DECIMAL_YEAR_VS_JULIAN_EPOCH"],
        ),
        "2C.1-EXP-03": (
            "2C.1-EXP-03-BATCH01-SYNTHETIC",
            ["BESSELIAN_REJECTION_GUARD"],
        ),
    },
    "ROUTE_AND_CONVENTION_CONSISTENCY": {
        "2C.2-EXP-01": (
            "2C.2-EXP-01-BATCH01-SYNTHETIC",
            ["DECOMPOSED_VS_COMPOSED_IDENTICAL_SYNTHETIC_INPUTS"],
        )
    },
    "MOTION_CONVENTION_GUARDS": {
        "2C.2-EXP-04": (
            "2C.2-EXP-04-BATCH01-SYNTHETIC-CONVENTION-GUARDS",
            [
                "OMITTED_COSINE_GUARD",
                "DOUBLE_COSINE_GUARD",
                "DECLARED_TARGET_EPOCH_LABEL_GUARD",
                "TWO_PART_JD_SPLIT_INVARIANT",
                "WARNING_STATUS_PRESERVATION",
            ],
        )
    },
    "DETERMINISTIC_REPLAY": {
        "2C.3-EXP-01": (
            "2C.3-EXP-01-BATCH01-SYNTHETIC",
            [
                "TWO_RUN_CANONICAL_REPLAY",
                "FRESH_ISOLATED_ENVIRONMENT_REPLAY",
            ],
        )
    },
    "OPTIONAL_STATE_GUARDS": {
        "2C.4-EXP-05": (
            "2C.4-EXP-05-BATCH01-SYNTHETIC",
            ["BELOW_HORIZON_GEOMETRIC_STATE_PRESERVATION"],
        ),
        "2C.4-EXP-06": (
            "2C.4-EXP-06-BATCH01-SYNTHETIC",
            ["NO_DEFAULT_ATMOSPHERE_GUARD"],
        ),
        "2C.4-EXP-07": (
            "2C.4-EXP-07-BATCH01-SYNTHETIC",
            ["VISIBILITY_COMPONENT_INDEPENDENCE"],
        ),
    },
}


def read_json(path: Path) -> dict:
    def reject_non_finite_constant(value: str) -> None:
        raise AssertionError(f"{path.name} contains non-JSON constant {value}")

    with path.open("r", encoding="utf-8") as source:
        value = json.load(source, parse_constant=reject_non_finite_constant)
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must contain an object")
    return value


def object_schema_paths(value: object, path: tuple[str, ...] = ()):
    if isinstance(value, dict):
        if value.get("type") == "object":
            yield path, value
        for key, child in value.items():
            yield from object_schema_paths(child, (*path, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from object_schema_paths(child, (*path, str(index)))


class ExperimentProtocolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = read_json(
            EXPERIMENT_ROOT / "experiment-registry.v1.json"
        )
        self.experiments = self.registry["experiments"]

    def test_registry_inventory_classifications_and_execution_guards(self) -> None:
        ids = [experiment["experimentId"] for experiment in self.experiments]
        self.assertEqual(ids, sorted(EXPECTED_EXPERIMENTS))
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(
            {
                experiment["experimentId"]: experiment[
                    "currentClassification"
                ]
                for experiment in self.experiments
            },
            EXPECTED_EXPERIMENTS,
        )

        counts = Counter(
            experiment["currentClassification"]
            for experiment in self.experiments
        )
        self.assertEqual(
            {
                classification: counts[classification]
                for classification in self.registry[
                    "classificationVocabulary"
                ]
            },
            EXPECTED_CLASSIFICATION_COUNTS,
        )

        for experiment in self.experiments:
            self.assertNotIn("SOURCE_DERIVED", experiment["inputClasses"])
            if experiment["currentClassification"] == "RUNNABLE_SYNTHETIC_NOW":
                self.assertIn("SYNTHETIC", experiment["inputClasses"])
                self.assertNotIn("SOURCE_DERIVED", experiment["inputClasses"])
                self.assertNotIn(
                    "PRODUCTION_GENERATED", experiment["inputClasses"]
                )
                self.assertNotEqual(
                    experiment["acceptanceMode"], "NOT_RUNNABLE"
                )
                self.assertEqual(experiment["blockers"], [])
            else:
                self.assertFalse(experiment["firstBatch"])
                self.assertEqual(
                    experiment["acceptanceMode"], "NOT_RUNNABLE"
                )
                self.assertGreaterEqual(len(experiment["blockers"]), 1)

    def test_human_classification_table_matches_machine_registry(self) -> None:
        protocol = (
            REPOSITORY_ROOT
            / "docs"
            / "spikes"
            / "PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md"
        ).read_text(encoding="utf-8")
        table = protocol.split("## Complete experiment classification", 1)[1]
        table = table.split("## Experiment records", 1)[0]
        rows = re.findall(
            r"^\| `(2C\.[1-4]-EXP-[0-9]{2})` \| ([^|]+?) \| `([A-Z_]+)` \|",
            table,
            flags=re.MULTILINE,
        )
        self.assertEqual(len(rows), 24)
        self.assertEqual(len({row[0] for row in rows}), 24)

        machine = {
            experiment["experimentId"]: (
                experiment["title"],
                experiment["currentClassification"],
            )
            for experiment in self.experiments
        }
        human = {
            experiment_id: (title.strip(), classification)
            for experiment_id, title, classification in rows
        }
        self.assertEqual(human, machine)

        all_human_ids = set(
            re.findall(r"`(2C\.[1-4]-EXP-[0-9]{2})`", protocol)
        )
        self.assertEqual(all_human_ids, set(EXPECTED_EXPERIMENTS))

    def test_batch_01_membership_and_bounded_scope_are_exact(self) -> None:
        batch = self.registry["firstBatch"]
        self.assertEqual(batch["batchId"], "2C.5B-BATCH-01")
        self.assertEqual(
            batch["status"], "PROPOSED_SYNTHETIC_EXECUTION_ONLY"
        )
        self.assertEqual(
            batch["inputClassification"], "SYNTHETIC_EXPERIMENT_INPUT"
        )
        self.assertEqual(
            batch["prohibitedInputClasses"],
            ["SOURCE_DERIVED", "PRODUCTION_GENERATED"],
        )
        self.assertEqual(
            batch["prohibitedSourceMaterial"],
            [
                "I311_CATALOGUE_ROWS",
                "HIP_SOURCE_DERIVED_VALUES",
                "CATALOGUE_SOURCE_BYTES",
            ],
        )
        self.assertEqual(
            batch["prohibitedClaims"],
            [
                "I311_EPOCH_TIME_SCALE_RESOLVED",
                "PRODUCTION_APPROVAL",
                "INDEPENDENT_SCIENTIFIC_VALIDATION_FROM_SHARED_LINEAGE",
                "SCIENTIFIC_TOLERANCE_ACCEPTED",
            ],
        )
        self.assertEqual(
            [group["groupId"] for group in batch["executionGroups"]],
            list(EXPECTED_BATCH),
        )

        actual: dict[str, dict[str, tuple[str, list[str]]]] = {}
        for group in batch["executionGroups"]:
            actual[group["groupId"]] = {
                member["experimentId"]: (
                    member["scopeId"],
                    member["includedPartitions"],
                )
                for member in group["members"]
            }
        self.assertEqual(actual, EXPECTED_BATCH)

        batch_ids = {
            experiment_id
            for members in actual.values()
            for experiment_id in members
        }
        self.assertEqual(len(batch_ids), 9)
        self.assertEqual(
            batch_ids,
            {
                experiment["experimentId"]
                for experiment in self.experiments
                if experiment["firstBatch"]
            },
        )
        self.assertTrue(
            all(
                EXPECTED_EXPERIMENTS[experiment_id]
                == "RUNNABLE_SYNTHETIC_NOW"
                for experiment_id in batch_ids
            )
        )

    def test_schema_versions_closed_objects_and_synthetic_scope(self) -> None:
        schemas = {
            "registry": read_json(
                EXPERIMENT_ROOT / "experiment-registry.v1.schema.json"
            ),
            "fixture": read_json(
                EXPERIMENT_ROOT / "experiment-fixture.v1.schema.json"
            ),
            "result": read_json(
                EXPERIMENT_ROOT / "experiment-result.v1.schema.json"
            ),
        }
        expected_ids = {
            "registry": "urn:ufuq:astronomy-experiment-registry:v1",
            "fixture": "urn:ufuq:astronomy-experiment-fixture:v1",
            "result": "urn:ufuq:astronomy-experiment-result:v1",
        }
        for name, schema in schemas.items():
            self.assertEqual(
                schema["$schema"],
                "https://json-schema.org/draft/2020-12/schema",
            )
            self.assertEqual(schema["$id"], expected_ids[name])
            self.assertFalse(schema["additionalProperties"])
            self.assertGreater(len(schema["required"]), 0)
            for path, object_schema in object_schema_paths(schema):
                if path == ("properties", "inputs"):
                    self.assertEqual(
                        object_schema["additionalProperties"],
                        {"$ref": "#/$defs/syntheticInput"},
                    )
                else:
                    self.assertFalse(
                        object_schema.get("additionalProperties", False),
                        f"open object schema at {'/'.join(path)}",
                    )

        registry_schema = schemas["registry"]
        fixture_schema = schemas["fixture"]
        result_schema = schemas["result"]
        self.assertEqual(
            self.registry["schemaVersion"],
            registry_schema["properties"]["schemaVersion"]["const"],
        )
        self.assertEqual(
            self.registry["protocolVersion"],
            fixture_schema["properties"]["protocolVersion"]["const"],
        )
        self.assertEqual(
            self.registry["fixtureSchema"],
            fixture_schema["properties"]["schemaVersion"]["const"],
        )
        self.assertEqual(
            self.registry["resultSchema"],
            result_schema["properties"]["schemaVersion"]["const"],
        )
        result_manifest_properties = result_schema["$defs"][
            "executionManifest"
        ]["properties"]
        self.assertEqual(
            result_manifest_properties["protocolVersion"]["const"],
            self.registry["protocolVersion"],
        )
        self.assertEqual(
            result_manifest_properties["registryVersion"]["const"],
            self.registry["schemaVersion"],
        )
        self.assertEqual(
            set(registry_schema["$defs"]["experimentId"]["enum"]),
            set(EXPECTED_EXPERIMENTS),
        )
        self.assertEqual(
            set(
                registry_schema["$defs"]["experiment"]["properties"][
                    "currentClassification"
                ]["enum"]
            ),
            set(self.registry["classificationVocabulary"]),
        )
        self.assertEqual(
            set(
                registry_schema["$defs"]["experiment"]["properties"][
                    "comparisonLineage"
                ]["enum"]
            ),
            set(result_manifest_properties["comparisonLineage"]["enum"]),
        )
        runnable_ids = {
            experiment_id
            for experiment_id, classification in EXPECTED_EXPERIMENTS.items()
            if classification == "RUNNABLE_SYNTHETIC_NOW"
        }
        self.assertEqual(
            set(fixture_schema["$defs"]["runnableExperimentId"]["enum"]),
            runnable_ids,
        )
        self.assertEqual(
            set(result_schema["$defs"]["runnableExperimentId"]["enum"]),
            runnable_ids,
        )
        self.assertEqual(
            fixture_schema["properties"]["inputClassification"]["const"],
            "SYNTHETIC_EXPERIMENT_INPUT",
        )
        for value in fixture_schema["properties"]["sourceProhibitions"][
            "properties"
        ].values():
            self.assertIs(value["const"], True)
        synthetic_input = fixture_schema["$defs"]["syntheticInput"]
        self.assertIn("inputIntent", synthetic_input["required"])
        self.assertEqual(
            synthetic_input["properties"]["inputIntent"]["enum"],
            [
                "VALID_VALUE",
                "DELIBERATELY_INVALID_TOKEN",
                "DELIBERATELY_MISSING",
            ],
        )
        self.assertEqual(
            synthetic_input["allOf"][1]["then"]["properties"]["value"][
                "const"
            ],
            "MISSING",
        )
        self.assertNotIn(
            "minItems",
            fixture_schema["properties"]["usedArtifactHashes"],
        )
        self.assertEqual(
            result_schema["properties"]["resultClassification"]["const"],
            "SYNTHETIC_EXPERIMENT_EVIDENCE_ONLY",
        )
        self.assertEqual(
            result_schema["properties"]["errorBudgetStatus"]["const"],
            "NOT_ESTABLISHED_AST_006_OPEN",
        )

    def test_result_outcomes_manifest_and_acceptance_are_fail_closed(self) -> None:
        result_schema = read_json(
            EXPERIMENT_ROOT / "experiment-result.v1.schema.json"
        )
        outcome = result_schema["$defs"]["executionOutcome"]
        self.assertEqual(
            outcome["properties"]["state"]["enum"],
            ["COMPLETED", "BLOCKED", "SKIPPED", "EXECUTION_ERROR"],
        )

        manifest = result_schema["$defs"]["executionManifest"]
        self.assertTrue(
            {
                "experimentId",
                "fixtureId",
                "caseId",
                "protocolVersion",
                "registryVersion",
                "fixtureSchemaVersion",
                "resultSchemaVersion",
                "hashes",
                "softwareRuntime",
                "runtimeContext",
                "runner",
                "externalArtifactProvenance",
                "canonicalSerialization",
                "recordOrdering",
            }.issubset(manifest["required"])
        )
        hashes = result_schema["$defs"]["executionHashes"]["required"]
        self.assertTrue(
            {
                "protocolDocumentSha256",
                "registrySha256",
                "registrySchemaSha256",
                "fixtureSchemaSha256",
                "resultSchemaSha256",
                "environmentManifestSha256",
                "lockfileSha256",
                "fixtureByteLength",
                "fixtureSha256",
            }.issubset(hashes)
        )
        self.assertEqual(
            manifest["properties"]["canonicalSerialization"]["const"],
            "UFUQ_CANONICAL_JSON_V1",
        )
        self.assertNotIn(
            "minItems",
            manifest["properties"]["externalArtifactProvenance"],
        )

        protocol = (
            REPOSITORY_ROOT
            / "docs"
            / "spikes"
            / "PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md"
        ).read_text(encoding="utf-8")
        for required_canonicalization_pattern in (
            r"UTF-8 without a byte-order mark",
            r"LF\s+line endings",
            r"shortest decimal that",
            r"Array order is semantic",
            r"Byte identity establishes deterministic serialization and replay only",
        ):
            self.assertRegex(protocol, required_canonicalization_pattern)

        check_schema = result_schema["$defs"]["check"]
        self.assertEqual(
            check_schema["properties"]["numericalThreshold"]["type"],
            "null",
        )
        status_guard = check_schema["allOf"][0]
        self.assertEqual(
            status_guard["then"]["properties"]["status"]["enum"],
            ["PASS", "FAIL", "NOT_RUN"],
        )
        self.assertEqual(
            status_guard["then"]["properties"]["basisClassification"][
                "enum"
            ],
            ["SOURCE_SUPPORTED_FACT", "PROJECT_DECISION"],
        )
        self.assertEqual(
            status_guard["else"]["properties"]["status"]["enum"],
            ["MEASURED_NO_ACCEPTANCE", "NOT_RUN"],
        )
        self.assertEqual(
            status_guard["else"]["properties"]["basisClassification"][
                "const"
            ],
            "MEASUREMENT_PROTOCOL",
        )

    def test_all_local_schema_references_resolve(self) -> None:
        for schema_path in EXPERIMENT_ROOT.glob("*.schema.json"):
            schema = read_json(schema_path)
            definitions = schema.get("$defs", {})

            def walk(value: object) -> None:
                if isinstance(value, dict):
                    reference = value.get("$ref")
                    if isinstance(reference, str) and reference.startswith(
                        "#/$defs/"
                    ):
                        self.assertIn(
                            reference.removeprefix("#/$defs/"),
                            definitions,
                            f"unresolved reference in {schema_path.name}",
                        )
                    for child in value.values():
                        walk(child)
                elif isinstance(value, list):
                    for child in value:
                        walk(child)

            walk(schema)

    def test_2c5a_has_no_direct_erfa_import_or_experiment_instances(self) -> None:
        self.assertEqual(
            {path.name for path in EXPERIMENT_ROOT.iterdir() if path.is_file()},
            {
                "experiment-fixture.v1.schema.json",
                "experiment-registry.v1.json",
                "experiment-registry.v1.schema.json",
                "experiment-result.v1.schema.json",
            },
        )
        pyproject = (PROJECT_ROOT / "pyproject.toml").read_text(
            encoding="utf-8"
        )
        dependency_block = pyproject.split("dependencies = [", 1)[1].split(
            "]", 1
        )[0]
        self.assertNotIn("pyerfa", dependency_block.casefold())

        for python_file in PROJECT_ROOT.rglob("*.py"):
            if ".venv" in python_file.parts or "__pycache__" in python_file.parts:
                continue
            tree = ast.parse(python_file.read_text(encoding="utf-8"))
            imported_modules = {
                alias.name.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.Import)
                for alias in node.names
            }
            imported_modules.update(
                node.module.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module is not None
            )
            self.assertNotIn("erfa", imported_modules, str(python_file))


if __name__ == "__main__":
    unittest.main()
