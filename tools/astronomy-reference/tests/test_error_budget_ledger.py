from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
EXPERIMENT_ROOT = PROJECT_ROOT / "experiments"
LEDGER_PATH = (
    REPOSITORY_ROOT
    / "docs"
    / "governance"
    / "AST_006_ERROR_BUDGET_LEDGER.v1.json"
)

GOVERNANCE_ID_PATHS = (
    REPOSITORY_ROOT / "docs" / "governance" / "OPEN_QUESTIONS.md",
    REPOSITORY_ROOT / "docs" / "references" / "SOURCE_GAPS.md",
    REPOSITORY_ROOT / "docs" / "IMPLEMENTATION_DECISIONS.md",
)

EXPECTED_LAYER_TERM_COUNTS = {
    "A_SOURCE_CATALOGUE": 6,
    "B_PROPAGATION_MODEL": 9,
    "C_EARTH_ORIENTATION_TIME": 9,
    "D_OBSERVER": 6,
    "E_ATMOSPHERE_REFRACTION": 7,
    "F_NUMERICAL_IMPLEMENTATION": 6,
    "G_SCENE_RENDER": 3,
    "H_LEARNER_ASSESSMENT": 3,
}

EXPECTED_TERM_PREFIX_LAYERS = {
    "A": "A_SOURCE_CATALOGUE",
    "B": "B_PROPAGATION_MODEL",
    "C": "C_EARTH_ORIENTATION_TIME",
    "D": "D_OBSERVER",
    "E": "E_ATMOSPHERE_REFRACTION",
    "F": "F_NUMERICAL_IMPLEMENTATION",
    "G": "G_SCENE_RENDER",
    "H": "H_LEARNER_ASSESSMENT",
}

EXPECTED_EXACT_GUARD_TERMS = {
    "AST006-F-002",
    "AST006-F-003",
    "AST006-F-004",
    "AST006-F-006",
}

EXPECTED_CLASSIFICATIONS = {
    "EXACT_CONTRACT_INVARIANT",
    "MEASURED_SYNTHETIC_SENSITIVITY",
    "SOURCE_UNCERTAINTY_UNRESOLVED",
    "MODEL_UNCERTAINTY_UNRESOLVED",
    "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED",
    "IMPLEMENTATION_ERROR_UNMEASURED",
    "INDEPENDENT_VALIDATION_REQUIRED",
    "HUMAN_REVIEW_REQUIRED",
    "CANDIDATE_TOLERANCE_PROPOSAL",
    "FINAL_TOLERANCE_NOT_JUSTIFIED",
}

EXPECTED_TOLERANCE_CLASSES = {
    "ScientificReferenceTolerance",
    "ProductionImplementationTolerance",
    "ScenarioGenerationTolerance",
    "SceneAngularTolerance",
    "LearnerInteractionTolerance",
    "AssessmentScoringTolerance",
}

EXPECTED_VALUE_CATEGORIES = {
    "MEASURED_VALUE",
    "MATHEMATICAL_EXACTNESS",
    "SOURCE_DECLARED_UNCERTAINTY",
    "EXTERNAL_AUTHORITY_LIMIT",
    "CANDIDATE_ENGINEERING_ALLOWANCE",
    "SCIENTIFICALLY_APPROVED_ACCEPTANCE_THRESHOLD",
}

EXPECTED_RANKED_EXPERIMENTS = [
    "2C.3-EXP-02",
    "2C.3-EXP-05",
    "2C.3-EXP-04",
    "2C.2-EXP-03",
    "2C.2-EXP-06",
    "2C.4-EXP-03",
    "2C.4-EXP-02",
    "2C.4-EXP-04",
]

EXPECTED_MEASUREMENT_SEMANTICS = {
    **{
        f"AST006-M-{index:03d}": (True, False, False, "NONE_SHARED_LINEAGE")
        for index in (1, 4, 9, 16, 17, 18, 19)
    },
    **{
        f"AST006-M-{index:03d}": (
            True,
            True,
            False,
            "DESCRIPTIVE_CANDIDATE_INPUT_NOT_COMBINABLE",
        )
        for index in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13)
    },
    **{
        f"AST006-M-{index:03d}": (
            False,
            True,
            True,
            "NONE_REJECTED_REPRESENTATION",
        )
        for index in (14, 15)
    },
    **{
        f"AST006-M-{index:03d}": (
            True,
            False,
            True,
            "NONE_GUARD_DIAGNOSTIC",
        )
        for index in (20, 21, 22, 23, 24)
    },
    "AST006-M-025": (False, False, True, "NONE_REPRODUCIBILITY"),
    "AST006-M-026": (False, False, True, "NONE_REPRODUCIBILITY"),
    "AST006-M-027": (False, False, True, "NONE_STRUCTURAL_STATE"),
}

EXPECTED_TERM_STATUSES = {
    **{
        f"AST006-A-{index:03d}": "SOURCE_UNCERTAINTY_UNRESOLVED"
        for index in range(1, 7)
    },
    **{
        f"AST006-B-{index:03d}": "MODEL_UNCERTAINTY_UNRESOLVED"
        for index in range(1, 10)
    },
    **{
        f"AST006-C-{index:03d}": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED"
        for index in range(1, 9)
    },
    "AST006-C-009": "HUMAN_REVIEW_REQUIRED",
    "AST006-D-001": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED",
    "AST006-D-002": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED",
    "AST006-D-003": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED",
    "AST006-D-004": "HUMAN_REVIEW_REQUIRED",
    "AST006-D-005": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED",
    "AST006-D-006": "HUMAN_REVIEW_REQUIRED",
    "AST006-E-001": "MODEL_UNCERTAINTY_UNRESOLVED",
    **{
        f"AST006-E-{index:03d}": "OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED"
        for index in range(2, 6)
    },
    "AST006-E-006": "MODEL_UNCERTAINTY_UNRESOLVED",
    "AST006-E-007": "MODEL_UNCERTAINTY_UNRESOLVED",
    "AST006-F-001": "IMPLEMENTATION_ERROR_UNMEASURED",
    "AST006-F-002": "EXACT_CONTRACT_INVARIANT",
    "AST006-F-003": "EXACT_CONTRACT_INVARIANT",
    "AST006-F-004": "EXACT_CONTRACT_INVARIANT",
    "AST006-F-005": "INDEPENDENT_VALIDATION_REQUIRED",
    "AST006-F-006": "EXACT_CONTRACT_INVARIANT",
    **{
        f"AST006-G-{index:03d}": "IMPLEMENTATION_ERROR_UNMEASURED"
        for index in range(1, 4)
    },
    **{
        f"AST006-H-{index:03d}": "HUMAN_REVIEW_REQUIRED"
        for index in range(1, 4)
    },
}

HASH_INPUTS = {
    "protocolDocumentSha256": (
        REPOSITORY_ROOT
        / "docs"
        / "spikes"
        / "PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md"
    ),
    "registrySha256": EXPERIMENT_ROOT / "experiment-registry.v1.json",
    "registrySchemaSha256": (
        EXPERIMENT_ROOT / "experiment-registry.v1.schema.json"
    ),
    "fixtureSchemaSha256": (
        EXPERIMENT_ROOT / "experiment-fixture.v1.schema.json"
    ),
    "resultSchemaSha256": (
        EXPERIMENT_ROOT / "experiment-result.v1.schema.json"
    ),
    "environmentManifestSha256": PROJECT_ROOT / "environment-manifest.json",
    "lockfileSha256": PROJECT_ROOT / "uv.lock",
    "batchRunnerSha256": (
        PROJECT_ROOT / "src" / "ufuq_astronomy_reference" / "batch01.py"
    ),
    "protocolValidatorSha256": (
        PROJECT_ROOT
        / "src"
        / "ufuq_astronomy_reference"
        / "experiment_protocol.py"
    ),
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_number_or_null(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, dict):
        return any(contains_number_or_null(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_number_or_null(item) for item in value)
    return False


class ErrorBudgetLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
        cls.human_document_path = REPOSITORY_ROOT / cls.ledger["humanDocument"]
        cls.human_document = cls.human_document_path.read_text(encoding="utf-8")
        cls.registry = json.loads(
            (EXPERIMENT_ROOT / "experiment-registry.v1.json").read_text(
                encoding="utf-8"
            )
        )
        cls.fixtures: dict[str, tuple[Path, dict]] = {}
        for path in sorted((EXPERIMENT_ROOT / "fixtures" / "batch-01").glob("*.json")):
            fixture = json.loads(path.read_text(encoding="utf-8"))
            cls.fixtures[fixture["fixtureId"]] = (path, fixture)
        cls.results: dict[str, dict] = {}
        for record in cls.ledger["batch01Evidence"]["resultFiles"]:
            path = REPOSITORY_ROOT / record["path"]
            cls.results[record["experimentId"]] = json.loads(
                path.read_text(encoding="utf-8")
            )
        cls.documented_governance_ids = set()
        governance_id_pattern = re.compile(
            r"\b(?:AST-SRC|DATA-SRC|AST|ACC|IMP)-\d{3}\b"
        )
        for path in GOVERNANCE_ID_PATHS:
            cls.documented_governance_ids.update(
                governance_id_pattern.findall(path.read_text(encoding="utf-8"))
            )

    def test_frozen_batch_hashes_and_result_companions_match(self) -> None:
        evidence = self.ledger["batch01Evidence"]
        for field, path in HASH_INPUTS.items():
            with self.subTest(field=field):
                self.assertEqual(evidence[field], sha256_file(path))

        self.assertEqual(len(evidence["resultFiles"]), 9)
        self.assertEqual(len(self.fixtures), 9)
        for record in evidence["resultFiles"]:
            path = REPOSITORY_ROOT / record["path"]
            companion = path.with_suffix(".sha256")
            actual = sha256_file(path)
            self.assertEqual(record["sha256"], actual)
            self.assertEqual(companion.read_text(encoding="ascii").strip(), actual)
            result = self.results[record["experimentId"]]
            self.assertEqual(result["experimentId"], record["experimentId"])
            self.assertEqual(result["fixtureId"], record["fixtureId"])

            fixture_path, _fixture = self.fixtures[result["fixtureId"]]
            manifest = result["executionManifest"]
            hashes = manifest["hashes"]
            self.assertEqual(hashes["fixtureSha256"], sha256_file(fixture_path))
            self.assertEqual(hashes["fixtureByteLength"], len(fixture_path.read_bytes()))
            for field in (
                "protocolDocumentSha256",
                "registrySha256",
                "registrySchemaSha256",
                "fixtureSchemaSha256",
                "resultSchemaSha256",
                "environmentManifestSha256",
                "lockfileSha256",
            ):
                self.assertEqual(hashes[field], evidence[field])

            for source in manifest["runner"]["sourceFiles"]:
                source_path = PROJECT_ROOT / source["path"]
                self.assertEqual(source["sha256"], sha256_file(source_path))

    def test_derived_batch_totals_match_canonical_results(self) -> None:
        outcomes = Counter()
        exact = Counter()
        measurement_checks = 0
        measurement_records = 0
        for result in self.results.values():
            outcomes[result["executionOutcome"]["state"]] += 1
            measurement_records += len(result["measurements"])
            for check in result["checks"]:
                if check["kind"] == "EXACT_INVARIANT":
                    exact[check["status"]] += 1
                elif check["kind"] == "MEASUREMENT_ONLY":
                    measurement_checks += 1

        self.assertEqual(outcomes, {"COMPLETED": 9})
        self.assertEqual(exact, {"PASS": 24})
        totals = self.ledger["batch01Evidence"]["derivedTotals"]
        self.assertEqual(totals["completedExperiments"], 9)
        self.assertEqual(totals["exactInvariantPass"], 24)
        self.assertEqual(totals["exactInvariantFail"], 0)
        self.assertEqual(totals["measurementOnlyChecks"], measurement_checks)
        self.assertEqual(totals["measuredNoAcceptanceRecords"], measurement_records)
        self.assertEqual(measurement_checks, 6)
        self.assertEqual(measurement_records, 27)

    def test_all_27_measurements_are_exactly_inventoried(self) -> None:
        actual: dict[tuple[str, str], dict] = {}
        for experiment_id, result in self.results.items():
            lineage = result["executionManifest"]["comparisonLineage"]
            for measurement in result["measurements"]:
                self.assertEqual(
                    measurement["acceptanceStatus"],
                    "MEASURED_NO_ACCEPTANCE",
                )
                actual[(experiment_id, measurement["measurementId"])] = {
                    "fixtureId": result["fixtureId"],
                    "metric": measurement["metric"],
                    "unit": measurement["unit"],
                    "value": measurement["value"],
                    "scientificLineage": lineage,
                }

        inventoried = {}
        for measurement in self.ledger["measurements"]:
            key = (measurement["experimentId"], measurement["measurementId"])
            self.assertNotIn(key, inventoried)
            inventoried[key] = {
                "fixtureId": measurement["fixtureId"],
                "metric": measurement["metric"],
                "unit": measurement["unit"],
                "value": measurement["value"],
                "scientificLineage": measurement["scientificLineage"],
            }
            self.assertEqual(measurement["valueCategory"], "MEASURED_VALUE")
            self.assertEqual(
                measurement["status"], "MEASURED_SYNTHETIC_SENSITIVITY"
            )
            semantics = (
                measurement["sameFamily"],
                measurement["sensitivityMeasurement"],
                measurement["exactConventionGuardContext"],
                measurement["budgetUse"],
            )
            self.assertEqual(
                semantics,
                EXPECTED_MEASUREMENT_SEMANTICS[measurement["id"]],
            )
            self.assertEqual(
                measurement["scientificLineage"],
                "SAME_ERFA_SOFA_FAMILY"
                if measurement["sameFamily"]
                else "STRUCTURAL_INVARIANT",
            )

        self.assertEqual(len(inventoried), 27)
        self.assertEqual(
            {measurement["id"] for measurement in self.ledger["measurements"]},
            set(EXPECTED_MEASUREMENT_SEMANTICS),
        )
        self.assertEqual(inventoried, actual)
        self.assertEqual(
            Counter(item["budgetUse"] for item in self.ledger["measurements"]),
            {
                "NONE_SHARED_LINEAGE": 7,
                "DESCRIPTIVE_CANDIDATE_INPUT_NOT_COMBINABLE": 10,
                "NONE_REJECTED_REPRESENTATION": 2,
                "NONE_GUARD_DIAGNOSTIC": 5,
                "NONE_REPRODUCIBILITY": 2,
                "NONE_STRUCTURAL_STATE": 1,
            },
        )

    def test_all_24_exact_invariants_are_inventoried_without_bounds(self) -> None:
        actual = set()
        for experiment_id, result in self.results.items():
            for check in result["checks"]:
                if check["kind"] != "EXACT_INVARIANT":
                    continue
                self.assertIsNone(check["numericalThreshold"])
                actual.add((experiment_id, check["checkId"], check["status"]))

        inventoried = {
            (item["experimentId"], item["checkId"], item["result"])
            for item in self.ledger["exactInvariants"]
        }
        invariant_records = self.ledger["exactInvariants"]
        self.assertEqual(len(invariant_records), 24)
        self.assertEqual(
            {item["id"] for item in invariant_records},
            {f"AST006-I-{index:03d}" for index in range(1, 25)},
        )
        self.assertTrue(
            all(item["mistakeClassRetired"] for item in invariant_records)
        )
        self.assertTrue(all(item["cannotRetire"] for item in invariant_records))
        self.assertEqual(len(inventoried), 24)
        self.assertEqual(inventoried, actual)
        self.assertTrue(
            all(
                item["status"] == "EXACT_CONTRACT_INVARIANT"
                for item in self.ledger["exactInvariants"]
            )
        )

    def test_terms_are_complete_unbounded_and_layer_separated(self) -> None:
        layers = {layer["id"] for layer in self.ledger["layers"]}
        self.assertEqual(len(self.ledger["layers"]), 8)
        self.assertEqual(
            layers,
            {
                "A_SOURCE_CATALOGUE",
                "B_PROPAGATION_MODEL",
                "C_EARTH_ORIENTATION_TIME",
                "D_OBSERVER",
                "E_ATMOSPHERE_REFRACTION",
                "F_NUMERICAL_IMPLEMENTATION",
                "G_SCENE_RENDER",
                "H_LEARNER_ASSESSMENT",
            },
        )
        required_fields = {
            "id",
            "layer",
            "quantity",
            "sourceAuthority",
            "status",
            "units",
            "bound",
            "distributionCorrelationAssumption",
            "affectedTransformationStage",
            "supportedDomain",
            "evidenceIds",
            "contributesToCombinedBudget",
            "reviewer",
            "approvalState",
        }
        ids = set()
        terms_by_id = {}
        for term in self.ledger["terms"]:
            self.assertEqual(set(term), required_fields)
            self.assertNotIn(term["id"], ids)
            ids.add(term["id"])
            terms_by_id[term["id"]] = term
            self.assertIn(term["layer"], layers)
            term_id_match = re.fullmatch(r"AST006-([A-H])-\d{3}", term["id"])
            self.assertIsNotNone(term_id_match)
            assert term_id_match is not None
            self.assertEqual(
                term["layer"],
                EXPECTED_TERM_PREFIX_LAYERS[term_id_match.group(1)],
            )
            self.assertIn(term["status"], EXPECTED_CLASSIFICATIONS)
            self.assertFalse(term["contributesToCombinedBudget"])
            self.assertNotIn("value", term["bound"])
            self.assertFalse(contains_number_or_null(term["bound"]))
            self.assertTrue(term["evidenceIds"])
            if term["status"] != "EXACT_CONTRACT_INVARIANT":
                self.assertEqual(
                    term["bound"]["state"], "UNBOUNDED_UNRESOLVED"
                )
                self.assertTrue(term["approvalState"].startswith("NOT_APPROVED"))
            else:
                self.assertTrue(term["approvalState"].startswith("EXACT_GUARD"))
        self.assertEqual(len(ids), 49)
        self.assertEqual(ids, set(EXPECTED_TERM_STATUSES))
        self.assertEqual(
            {term_id: term["status"] for term_id, term in terms_by_id.items()},
            EXPECTED_TERM_STATUSES,
        )
        self.assertEqual(
            Counter(term["layer"] for term in self.ledger["terms"]),
            EXPECTED_LAYER_TERM_COUNTS,
        )
        exact_guard_ids = {
            term["id"]
            for term in self.ledger["terms"]
            if term["status"] == "EXACT_CONTRACT_INVARIANT"
        }
        self.assertEqual(exact_guard_ids, EXPECTED_EXACT_GUARD_TERMS)
        self.assertEqual(
            sum(
                term["bound"]["state"] == "UNBOUNDED_UNRESOLVED"
                for term in self.ledger["terms"]
            ),
            45,
        )

        self.assertEqual(
            terms_by_id["AST006-F-002"]["affectedTransformationStage"],
            ["PropagatedIcrsAstrometry"],
        )
        self.assertEqual(
            terms_by_id["AST006-F-003"]["quantity"],
            "Omitted-cosine and double-cosine adapter mutation guards",
        )
        self.assertNotIn(
            "ALL_ASTRONOMY_STAGES",
            terms_by_id["AST006-F-004"]["affectedTransformationStage"],
        )
        self.assertEqual(
            terms_by_id["AST006-G-002"]["evidenceIds"], ["AST-SRC-015"]
        )
        self.assertEqual(
            terms_by_id["AST006-G-003"]["evidenceIds"], ["AST-SRC-015"]
        )

        layer_flags = {
            layer["id"]: layer["partOfAstronomyScientificBudget"]
            for layer in self.ledger["layers"]
        }
        self.assertFalse(layer_flags["G_SCENE_RENDER"])
        self.assertFalse(layer_flags["H_LEARNER_ASSESSMENT"])
        layer_names = {layer["id"]: layer["name"] for layer in self.ledger["layers"]}
        self.assertEqual(
            layer_names["H_LEARNER_ASSESSMENT"],
            "Downstream scenario/learner/assessment tolerance",
        )
        self.assertTrue(
            all(
                layer_flags[layer]
                for layer in layers
                if layer not in {"G_SCENE_RENDER", "H_LEARNER_ASSESSMENT"}
            )
        )

    def test_term_evidence_ids_resolve_to_registered_or_documented_records(self) -> None:
        registry_ids = {
            item["experimentId"] for item in self.registry["experiments"]
        }
        canonical_check_ids = {
            (experiment_id, check["checkId"])
            for experiment_id, result in self.results.items()
            for check in result["checks"]
        }

        for term in self.ledger["terms"]:
            for evidence_id in term["evidenceIds"]:
                with self.subTest(term=term["id"], evidence=evidence_id):
                    if "/" in evidence_id:
                        experiment_id, check_id = evidence_id.split("/", 1)
                        self.assertIn(experiment_id, registry_ids)
                        self.assertIn(
                            (experiment_id, check_id), canonical_check_ids
                        )
                    elif evidence_id.startswith("2C."):
                        self.assertIn(evidence_id, registry_ids)
                    else:
                        self.assertIn(
                            evidence_id, self.documented_governance_ids
                        )

    def test_external_authority_limits_are_owned_by_their_declared_terms(self) -> None:
        terms_by_id = {term["id"]: term for term in self.ledger["terms"]}
        limits_by_id = {
            limit["id"]: limit for limit in self.ledger["externalAuthorityLimits"]
        }
        referenced_limits = set()

        for term in self.ledger["terms"]:
            for limit_id in term["bound"].get("externalAuthorityLimitIds", []):
                self.assertIn(limit_id, limits_by_id)
                self.assertEqual(limits_by_id[limit_id]["termId"], term["id"])
                referenced_limits.add(limit_id)

        self.assertEqual(referenced_limits, set(limits_by_id))
        for limit in limits_by_id.values():
            owner = terms_by_id[limit["termId"]]
            self.assertIn(
                limit["id"], owner["bound"]["externalAuthorityLimitIds"]
            )

    def test_human_document_cross_references_the_complete_ledger(self) -> None:
        self.assertEqual(
            self.ledger["humanDocument"],
            "docs/spikes/PHASE1_SCIENTIFIC_ERROR_BUDGET.md",
        )
        self.assertIn(LEDGER_PATH.name, self.human_document)
        self.assertIn("exactly 49 terms", self.human_document)
        self.assertIn("45 terms have an", self.human_document)
        self.assertIn("This count does not move", self.human_document)

        for measurement in self.ledger["measurements"]:
            evidence_id = (
                f"`{measurement['experimentId']}/"
                f"{measurement['measurementId']}`"
            )
            self.assertEqual(self.human_document.count(evidence_id), 1)

        for invariant in self.ledger["exactInvariants"]:
            evidence_id = (
                f"`{invariant['experimentId']} / {invariant['checkId']}`"
            )
            self.assertEqual(self.human_document.count(evidence_id), 1)

        for tolerance_name in EXPECTED_TOLERANCE_CLASSES:
            row_prefix = f"| `{tolerance_name}` | `BLOCKED` |"
            self.assertEqual(self.human_document.count(row_prefix), 1)

        self.assertIn("`FINAL_TOLERANCE_NOT_JUSTIFIED`", self.human_document)
        self.assertIn("Milestone 2C status:** `OPEN`", self.human_document)

    def test_no_tolerance_is_approved_or_numerically_populated(self) -> None:
        self.assertEqual(
            set(self.ledger["classificationVocabulary"]),
            EXPECTED_CLASSIFICATIONS,
        )
        self.assertEqual(
            set(self.ledger["numericalValueCategories"]),
            EXPECTED_VALUE_CATEGORIES,
        )
        self.assertEqual(self.ledger["status"], "REVIEW_REQUIRED")
        self.assertEqual(
            self.ledger["recommendation"], "FINAL_TOLERANCE_NOT_JUSTIFIED"
        )
        self.assertFalse(
            self.ledger["finalNumericalScientificToleranceApproved"]
        )
        self.assertEqual(
            self.ledger["combinedScientificBudgetState"],
            "UNBOUNDED_UNRESOLVED",
        )
        tolerances = self.ledger["toleranceClasses"]
        self.assertEqual(
            {item["name"] for item in tolerances},
            EXPECTED_TOLERANCE_CLASSES,
        )
        for tolerance in tolerances:
            self.assertEqual(tolerance["decisionStatus"], "BLOCKED")
            self.assertEqual(
                tolerance["classification"],
                "FINAL_TOLERANCE_NOT_JUSTIFIED",
            )
            self.assertEqual(
                tolerance["numericalValueState"], "NOT_ESTABLISHED"
            )
        self.assertEqual(
            self.ledger["candidateMethodology"]["status"],
            "CANDIDATE_TOLERANCE_PROPOSAL",
        )
        self.assertEqual(
            self.ledger["candidateMethodology"]["numericalThresholdState"],
            "NOT_ESTABLISHED",
        )
        methodology = self.ledger["candidateMethodology"]
        self.assertEqual(len(methodology["combinationRules"]), 7)
        self.assertTrue(any("root-sum-square" in rule for rule in methodology["combinationRules"]))
        self.assertTrue(any("covariance" in rule for rule in methodology["combinationRules"]))
        self.assertEqual(
            [item["boundary"] for item in methodology["metricHierarchy"]],
            [
                "CATALOGUE_OR_PROPAGATED_ICRS",
                "CELESTIAL_INTERMEDIATE_DIRECTION",
                "EARTH_ORIENTATION_TIME",
                "GEOMETRIC_HORIZONTAL",
                "HORIZON_AND_REFRACTION",
                "OBSERVER",
                "SCENE",
                "LEARNER_AND_SCORING",
            ],
        )
        self.assertEqual(
            self.ledger["externalAuthorityLimits"],
            [
                {
                    "id": "AST006-AUTH-LIMIT-001",
                    "termId": "AST006-E-007",
                    "valueCategory": "EXTERNAL_AUTHORITY_LIMIT",
                    "sourceAuthority": "ASTROPY-DOCS-PIN",
                    "approximateValue": 5,
                    "unit": "DEGREE",
                    "meaning": "Astropy 8.0.1 documents its ERFA-based refraction model as inaccurate below about this altitude.",
                    "projectDisposition": "REFERENCE_LIBRARY_LIMIT_ONLY_NOT_UFUQ_DOMAIN_BOUND_OR_ACCEPTANCE_THRESHOLD",
                }
            ],
        )
        self.assertEqual(self.ledger["review"]["approvalState"], "REVIEW_REQUIRED")
        self.assertEqual(self.ledger["review"]["openDecision"], "AST-006")
        self.assertEqual(self.ledger["review"]["milestone2CState"], "OPEN")

    def test_ranked_experiments_are_exactly_remaining_runnable_records(self) -> None:
        experiments = {
            item["experimentId"]: item for item in self.registry["experiments"]
        }
        remaining = {
            experiment_id
            for experiment_id, item in experiments.items()
            if item["currentClassification"] == "RUNNABLE_SYNTHETIC_NOW"
            and not item["firstBatch"]
        }
        ranked = self.ledger["rankedNextExperiments"]
        self.assertEqual([item["rank"] for item in ranked], list(range(1, 9)))
        self.assertEqual(
            [item["experimentId"] for item in ranked],
            EXPECTED_RANKED_EXPERIMENTS,
        )
        self.assertEqual({item["experimentId"] for item in ranked}, remaining)
        self.assertTrue(
            all(
                item["classification"] == "RUNNABLE_SYNTHETIC_NOW"
                for item in ranked
            )
        )


if __name__ == "__main__":
    unittest.main()
