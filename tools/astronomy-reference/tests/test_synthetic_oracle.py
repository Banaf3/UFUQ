from __future__ import annotations

import ast
import json
import re
import socket
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from ufuq_astronomy_reference import (  # noqa: E402
    UnexpectedNetworkAccess,
    build_environment_manifest,
    canonical_bytes,
    generate_fixture,
    sha256_bytes,
)
from ufuq_astronomy_reference.oracle import network_blocked  # noqa: E402


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must contain an object")
    return value


class SyntheticOracleTests(unittest.TestCase):
    input_path = PROJECT_ROOT / "fixtures" / "synthetic-input.v1.json"
    output_path = PROJECT_ROOT / "fixtures" / "synthetic-output.v1.json"
    output_hash_path = (
        PROJECT_ROOT / "fixtures" / "synthetic-output.v1.sha256"
    )
    environment_path = PROJECT_ROOT / "environment-manifest.json"

    def test_environment_manifest_matches_lock_and_runtime(self) -> None:
        expected = read_json(self.environment_path)
        actual = build_environment_manifest(PROJECT_ROOT)
        self.assertEqual(canonical_bytes(expected), canonical_bytes(actual))
        versions = {
            package["name"]: package["version"]
            for package in actual["resolvedRuntimePackages"]
        }
        self.assertEqual(versions["astropy"], "8.0.1")
        self.assertEqual(
            versions["astropy-iers-data"], "0.2026.7.20.15.31.18"
        )
        self.assertEqual(versions["numpy"], "2.5.1")
        self.assertEqual(versions["pyerfa"], "2.0.1.5")

    def test_valid_execution_and_structured_invalid_input(self) -> None:
        output = generate_fixture(
            read_json(self.input_path), read_json(self.environment_path)
        )
        self.assertEqual(len(output["cases"]), 3)
        self.assertEqual(
            [case["validity"] for case in output["cases"]],
            ["VALID", "VALID", "INVALID"],
        )
        invalid = output["cases"][2]
        self.assertEqual(
            invalid["error"]["code"], "INVALID_OBSERVER_LATITUDE"
        )
        for case in output["cases"][:2]:
            self.assertEqual(
                case["classification"], "SYNTHETIC_TEST_INPUT"
            )
            self.assertEqual(
                case["expected"]["coordinateState"],
                "GEOMETRIC_TOPOCENTRIC",
            )
            self.assertEqual(case["warnings"], [])
            body = dict(case)
            recorded = body.pop("canonicalContentSha256")
            self.assertEqual(recorded, sha256_bytes(canonical_bytes(body)))

    def test_deterministic_bytes_and_hash(self) -> None:
        input_document = read_json(self.input_path)
        environment = read_json(self.environment_path)
        first = canonical_bytes(generate_fixture(input_document, environment))
        second = canonical_bytes(generate_fixture(input_document, environment))
        expected = self.output_path.read_bytes()
        expected_hash = self.output_hash_path.read_text(
            encoding="ascii"
        ).strip()
        self.assertEqual(first, second)
        self.assertEqual(first, expected)
        self.assertEqual(sha256_bytes(first), expected_hash)

    def test_network_is_blocked_and_iers_policy_is_fail_closed(self) -> None:
        with network_blocked():
            with self.assertRaises(UnexpectedNetworkAccess):
                socket.create_connection(("example.invalid", 443))
        output = read_json(self.output_path)
        self.assertEqual(
            output["networkPolicy"],
            {
                "astropyAllowInternet": False,
                "astropyAutoDownload": False,
                "cacheIsolation": "FRESH_TEMPORARY_CACHE",
                "socketConnectionsBlocked": True,
            },
        )
        self.assertEqual(
            output["environmentEvidence"]["iersPolicy"][
                "degradedAccuracy"
            ],
            "error",
        )

    def test_prohibited_imports_and_repository_paths(self) -> None:
        prohibited_import_roots = {
            "apps",
            "packages",
            "astronomy_core",
            "assessment_core",
            "tutoring_core",
            "subprocess",
        }
        prohibited_path_fragments = {
            "data/raw",
            "node_modules",
            "/dist/",
            "\\dist\\",
        }
        sources = list((PROJECT_ROOT / "src").rglob("*.py")) + [
            PROJECT_ROOT / "run.py"
        ]
        for source in sources:
            text = source.read_text(encoding="utf-8")
            tree = ast.parse(text, filename=source.name)
            imports = {
                alias.name.split(".")[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.Import)
                for alias in node.names
            }
            imports.update(
                node.module.split(".")[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module
            )
            self.assertTrue(
                imports.isdisjoint(prohibited_import_roots),
                f"{source.name} has prohibited imports",
            )
            normalized = text.replace("\\\\", "\\")
            for fragment in prohibited_path_fragments:
                self.assertNotIn(fragment, normalized)

    def test_fixtures_contain_no_catalogue_identity_or_volatile_data(self) -> None:
        fixture_bytes = self.input_path.read_bytes() + self.output_path.read_bytes()
        fixture_text = fixture_bytes.decode("utf-8")
        forbidden = [
            r"\bHIP\s*\d",
            r"I/311",
            r"I/239",
            r"hip2\.dat",
            r"hip7p\.dat",
            r"hip9p\.dat",
            r"hipvim\.dat",
            r"\bPolaris\b",
            r"\bSirius\b",
            r"[A-Z]:\\",
            r"/home/",
            r'"generatedAt"',
            r'"executionDuration"',
        ]
        for pattern in forbidden:
            self.assertIsNone(
                re.search(pattern, fixture_text, flags=re.IGNORECASE)
            )
        source = read_json(self.input_path)
        generated = read_json(self.output_path)
        self.assertTrue(
            all(
                case["classification"] == "SYNTHETIC_TEST_INPUT"
                for case in source["cases"]
            )
        )
        self.assertTrue(
            all(
                case["classification"] == "SYNTHETIC_TEST_INPUT"
                for case in generated["cases"]
            )
        )

    def test_generation_does_not_depend_on_output_path(self) -> None:
        with (
            tempfile.TemporaryDirectory() as first_dir,
            tempfile.TemporaryDirectory() as second_dir,
        ):
            first = Path(first_dir) / "a.json"
            second = Path(second_dir) / "b.json"
            content = canonical_bytes(
                generate_fixture(
                    read_json(self.input_path),
                    read_json(self.environment_path),
                )
            )
            first.write_bytes(content)
            second.write_bytes(content)
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == "__main__":
    unittest.main()
