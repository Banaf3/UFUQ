"""Synthetic-only Astropy smoke oracle with explicit offline evidence.

This module intentionally accepts no catalogue input and imports no UFUQ production
package. Its outputs establish environment and execution-path reproducibility only.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import platform
import re
import socket
import sys
import tempfile
import tomllib
import urllib.request
import warnings
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from typing import Any
from unittest.mock import patch

import astropy.units as u
import astropy_iers_data
from astropy.config.paths import set_temp_cache
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.time import Time
from astropy.utils import iers
from astropy.utils.data import conf as data_conf

GENERATOR_NAME = "ufuq-astronomy-reference"
GENERATOR_VERSION = "0.1.0"
INPUT_SCHEMA_VERSION = "ufuq.synthetic-astronomy-input.v1"
OUTPUT_SCHEMA_VERSION = "ufuq.synthetic-astronomy-output.v1"
ENVIRONMENT_SCHEMA_VERSION = "ufuq.oracle-environment.v1"
SYNTHETIC_CLASSIFICATION = "SYNTHETIC_TEST_INPUT"
UV_VERSION = "0.11.32"

DIRECT_CONSTRAINTS = {
    "astropy": ">=8.0.1,<9",
    "astropy-iers-data": ">=0.2026.7.20.15.31.18,<0.2027",
}
RUNTIME_DISTRIBUTIONS = (
    "astropy",
    "astropy-iers-data",
    "numpy",
    "packaging",
    "pyerfa",
    "pyyaml",
)


class InputValidationError(ValueError):
    """A stable structured error for a rejected synthetic input."""

    def __init__(self, code: str, field: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field = field
        self.message = message

    def as_record(self) -> dict[str, str]:
        return {"code": self.code, "field": self.field, "message": self.message}


class UnexpectedNetworkAccess(RuntimeError):
    """Raised when smoke execution attempts any network connection."""


def canonical_bytes(value: Any) -> bytes:
    """Serialize canonical JSON as UTF-8, sorted compact keys, and one LF."""

    text = json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return (text + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _date_from_mjd(value: float) -> str:
    return str(Time(value, format="mjd", scale="utc").to_value("iso", subfmt="date"))


def _quantity_float(value: Any) -> float:
    raw = getattr(value, "value", value)
    return float(raw)


def _resource_record(path: Path, role: str) -> dict[str, Any]:
    return {
        "role": role,
        "packageResource": f"astropy_iers_data/data/{path.name}",
        "sha256": sha256_file(path),
        "sizeBytes": path.stat().st_size,
    }


def _iers_evidence() -> list[dict[str, Any]]:
    earth_path = Path(astropy_iers_data.IERS_A_FILE)
    earth_table = iers.IERS_A.open(str(earth_path))
    earth_record = _resource_record(earth_path, "EARTH_ORIENTATION")
    earth_record["coverage"] = {
        "startDateUtc": _date_from_mjd(_quantity_float(earth_table["MJD"][0])),
        "startMjd": _quantity_float(earth_table["MJD"][0]),
        "endDateUtc": _date_from_mjd(_quantity_float(earth_table["MJD"][-1])),
        "endMjd": _quantity_float(earth_table["MJD"][-1]),
        "predictiveStartDateUtc": _date_from_mjd(
            float(earth_table.meta["predictive_mjd"])
        ),
        "predictiveStartMjd": float(earth_table.meta["predictive_mjd"]),
    }

    leap_path = Path(astropy_iers_data.IERS_LEAP_SECOND_FILE)
    leap_table = iers.LeapSeconds.open(str(leap_path))
    leap_record = _resource_record(leap_path, "LEAP_SECONDS")
    comments = [str(comment) for comment in leap_table.meta.get("comments", [])]
    expiration = next(
        (
            match.group(1)
            for comment in comments
            if (match := re.match(r"File expires on (.+)", comment))
        ),
        None,
    )
    leap_record["coverage"] = {
        "firstEffectiveDateUtc": (
            f"{int(leap_table['year'][0]):04d}-"
            f"{int(leap_table['month'][0]):02d}-"
            f"{int(leap_table['day'][0]):02d}"
        ),
        "lastEffectiveDateUtc": (
            f"{int(leap_table['year'][-1]):04d}-"
            f"{int(leap_table['month'][-1]):02d}-"
            f"{int(leap_table['day'][-1]):02d}"
        ),
        "expiresAccordingToPackagedFile": expiration,
        "lastTaiMinusUtcSeconds": int(leap_table["tai_utc"][-1]),
    }
    return [earth_record, leap_record]


def _locked_versions(lock_path: Path) -> dict[str, str]:
    with lock_path.open("rb") as source:
        lock = tomllib.load(source)
    return {
        str(package["name"]): str(package["version"])
        for package in lock["package"]
        if "version" in package
    }


def build_environment_manifest(project_root: Path) -> dict[str, Any]:
    """Build stable lock, platform, package, and IERS evidence."""

    lock_path = project_root / "uv.lock"
    locked = _locked_versions(lock_path)
    resolved: list[dict[str, Any]] = []
    for name in RUNTIME_DISTRIBUTIONS:
        installed = importlib.metadata.version(name)
        expected = locked.get(name)
        if installed != expected:
            raise RuntimeError(
                f"Locked/installed version mismatch for {name}: "
                f"locked={expected!r}, installed={installed!r}"
            )
        resolved.append(
            {
                "name": name,
                "version": installed,
                "dependencyKind": "DIRECT"
                if name in DIRECT_CONSTRAINTS
                else "TRANSITIVE",
            }
        )

    return {
        "schemaVersion": ENVIRONMENT_SCHEMA_VERSION,
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
            "constraint": ">=3.14,<3.15",
            "compiler": platform.python_compiler(),
            "architecture": platform.architecture()[0],
        },
        "uv": {
            "version": UV_VERSION,
            "ordinaryMode": "--locked --no-sync",
            "synchronizationMode": "sync --locked --managed-python",
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
        },
        "lock": {
            "file": "uv.lock",
            "sha256": sha256_file(lock_path),
            "requiresPython": "==3.14.*",
        },
        "directDependencies": [
            {
                "name": name,
                "constraint": constraint,
                "reason": (
                    "Imported by the oracle"
                    if name == "astropy"
                    else "Imported directly so exact EOP/leap-second resources are evidenced"
                ),
            }
            for name, constraint in DIRECT_CONSTRAINTS.items()
        ],
        "resolvedRuntimePackages": resolved,
        "iersPolicy": {
            "autoDownload": False,
            "allowInternet": False,
            "degradedAccuracy": "error",
            "cachePolicy": "fresh temporary Astropy cache per execution",
            "files": _iers_evidence(),
            "dateRangeApproval": "NOT_ESTABLISHED_BY_THIS_SMOKE_MILESTONE",
        },
    }


def _environment_evidence(manifest: Mapping[str, Any]) -> dict[str, Any]:
    evidence = {
        "pythonVersion": manifest["python"]["version"],
        "uvVersion": manifest["uv"]["version"],
        "resolvedRuntimePackages": manifest["resolvedRuntimePackages"],
        "iersPolicy": manifest["iersPolicy"],
    }
    evidence["sha256"] = sha256_bytes(canonical_bytes(evidence))
    return evidence


def _blocked_network(*_args: Any, **_kwargs: Any) -> Any:
    raise UnexpectedNetworkAccess("Network access is blocked for oracle execution.")


@contextmanager
def network_blocked() -> Iterator[None]:
    """Fail closed if stdlib HTTP or socket connection APIs are reached."""

    with (
        patch("socket.create_connection", _blocked_network),
        patch.object(socket.socket, "connect", _blocked_network),
        patch.object(socket.socket, "connect_ex", _blocked_network),
        patch("urllib.request.urlopen", _blocked_network),
    ):
        yield


def _require_exact_keys(
    value: Mapping[str, Any], expected: set[str], field: str
) -> None:
    actual = set(value)
    if actual != expected:
        raise InputValidationError(
            "INVALID_STRUCTURE",
            field,
            f"Expected keys {sorted(expected)}, received {sorted(actual)}.",
        )


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputValidationError(
            "INVALID_NUMBER", field, "Value must be a finite JSON number."
        )
    number = float(value)
    if not math.isfinite(number):
        raise InputValidationError(
            "INVALID_NUMBER", field, "Value must be a finite JSON number."
        )
    return number


def _validate_case(case: Mapping[str, Any]) -> None:
    _require_exact_keys(
        case,
        {
            "caseId",
            "caseType",
            "classification",
            "expectedOutcome",
            "icrs",
            "referenceEpoch",
            "observationUtc",
            "observer",
            "pressureHpa",
        },
        "case",
    )
    case_id = case["caseId"]
    if not isinstance(case_id, str) or not re.fullmatch(
        r"synthetic-[a-z0-9-]+", case_id
    ):
        raise InputValidationError(
            "INVALID_CASE_ID",
            "caseId",
            "Case ID must use the synthetic- lowercase namespace.",
        )
    if case["classification"] != SYNTHETIC_CLASSIFICATION:
        raise InputValidationError(
            "INVALID_CLASSIFICATION",
            "classification",
            f"Classification must be {SYNTHETIC_CLASSIFICATION}.",
        )
    if case["caseType"] not in {"VALID_DIRECTION", "INVALID_INPUT"}:
        raise InputValidationError(
            "INVALID_CASE_TYPE",
            "caseType",
            "Case type must be VALID_DIRECTION or INVALID_INPUT.",
        )
    expected = (
        "VALID"
        if case["caseType"] == "VALID_DIRECTION"
        else "STRUCTURED_ERROR"
    )
    if case["expectedOutcome"] != expected:
        raise InputValidationError(
            "INVALID_EXPECTED_OUTCOME",
            "expectedOutcome",
            f"Expected outcome must be {expected}.",
        )
    if case["referenceEpoch"] != "J2000.0":
        raise InputValidationError(
            "UNSUPPORTED_SYNTHETIC_EPOCH",
            "referenceEpoch",
            "This smoke fixture supports only the explicit synthetic J2000.0 label.",
        )
    if not isinstance(case["observationUtc"], str) or not case[
        "observationUtc"
    ].endswith("Z"):
        raise InputValidationError(
            "INVALID_UTC_INSTANT",
            "observationUtc",
            "Observation time must be an ISO-8601 UTC string ending in Z.",
        )

    icrs = case["icrs"]
    if not isinstance(icrs, Mapping):
        raise InputValidationError("INVALID_STRUCTURE", "icrs", "Must be an object.")
    _require_exact_keys(icrs, {"raDegrees", "decDegrees"}, "icrs")
    ra = _finite_number(icrs["raDegrees"], "icrs.raDegrees")
    dec = _finite_number(icrs["decDegrees"], "icrs.decDegrees")
    if not 0.0 <= ra < 360.0:
        raise InputValidationError(
            "INVALID_RIGHT_ASCENSION",
            "icrs.raDegrees",
            "Right ascension must be within [0, 360) degrees.",
        )
    if not -90.0 <= dec <= 90.0:
        raise InputValidationError(
            "INVALID_DECLINATION",
            "icrs.decDegrees",
            "Declination must be within [-90, 90] degrees.",
        )

    observer = case["observer"]
    if not isinstance(observer, Mapping):
        raise InputValidationError(
            "INVALID_STRUCTURE", "observer", "Must be an object."
        )
    _require_exact_keys(
        observer,
        {
            "datum",
            "latitudeDegrees",
            "longitudeDegreesEast",
            "ellipsoidalHeightMeters",
        },
        "observer",
    )
    if observer["datum"] != "WGS84":
        raise InputValidationError(
            "INVALID_DATUM", "observer.datum", "Observer datum must be WGS84."
        )
    latitude = _finite_number(
        observer["latitudeDegrees"], "observer.latitudeDegrees"
    )
    longitude = _finite_number(
        observer["longitudeDegreesEast"], "observer.longitudeDegreesEast"
    )
    _finite_number(
        observer["ellipsoidalHeightMeters"],
        "observer.ellipsoidalHeightMeters",
    )
    if not -90.0 <= latitude <= 90.0:
        raise InputValidationError(
            "INVALID_OBSERVER_LATITUDE",
            "observer.latitudeDegrees",
            "Latitude must be within [-90, 90] degrees.",
        )
    if not -180.0 <= longitude <= 180.0:
        raise InputValidationError(
            "INVALID_OBSERVER_LONGITUDE",
            "observer.longitudeDegreesEast",
            "Longitude must be within [-180, 180] degrees.",
        )
    pressure = _finite_number(case["pressureHpa"], "pressureHpa")
    if pressure != 0.0:
        raise InputValidationError(
            "UNSUPPORTED_REFRACTION",
            "pressureHpa",
            "Synthetic smoke cases require pressure zero.",
        )


def _warning_records(caught: list[warnings.WarningMessage]) -> list[dict[str, str]]:
    records = {
        (warning.category.__name__, str(warning.message))
        for warning in caught
    }
    return [
        {"category": category, "message": message}
        for category, message in sorted(records)
    ]


def _canonical_degree(value: float) -> float:
    """Use round-trip decimal precision; this is serialization, not tolerance."""

    result = float(format(value, ".17g"))
    return 0.0 if result == 0.0 else result


def _valid_case_result(
    case: Mapping[str, Any], environment_sha256: str
) -> dict[str, Any]:
    observer = case["observer"]
    location = EarthLocation.from_geodetic(
        lon=float(observer["longitudeDegreesEast"]) * u.deg,
        lat=float(observer["latitudeDegrees"]) * u.deg,
        height=float(observer["ellipsoidalHeightMeters"]) * u.m,
        ellipsoid="WGS84",
    )
    instant = Time(str(case["observationUtc"]), scale="utc")
    direction = SkyCoord(
        ra=float(case["icrs"]["raDegrees"]) * u.deg,
        dec=float(case["icrs"]["decDegrees"]) * u.deg,
        frame="icrs",
    )
    frame = AltAz(
        obstime=instant,
        location=location,
        pressure=float(case["pressureHpa"]) * u.hPa,
    )
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        horizontal = direction.transform_to(frame)

    case_body: dict[str, Any] = {
        "caseId": case["caseId"],
        "classification": SYNTHETIC_CLASSIFICATION,
        "validity": "VALID",
        "input": deepcopy(dict(case)),
        "expected": {
            "altitude": {
                "value": _canonical_degree(horizontal.alt.to_value(u.deg)),
                "unit": "degree",
            },
            "azimuth": {
                "value": _canonical_degree(horizontal.az.to_value(u.deg)),
                "unit": "degree",
                "origin": "GEOGRAPHIC_TRUE_NORTH",
                "positiveDirection": "EASTWARD_CLOCKWISE",
            },
            "coordinateState": "GEOMETRIC_TOPOCENTRIC",
            "inputTimeScale": "UTC",
            "observerDatum": "WGS84",
            "spaceMotionPolicy": "NONE_SYNTHETIC_FIXED_ICRS_DIRECTION",
        },
        "warnings": _warning_records(caught),
        "environmentEvidenceSha256": environment_sha256,
    }
    case_body["canonicalContentSha256"] = sha256_bytes(
        canonical_bytes(case_body)
    )
    return case_body


def _invalid_case_result(
    case: Mapping[str, Any], error: InputValidationError
) -> dict[str, Any]:
    return {
        "caseId": case.get("caseId", "synthetic-invalid-unknown"),
        "classification": SYNTHETIC_CLASSIFICATION,
        "validity": "INVALID",
        "error": error.as_record(),
        "warnings": [],
    }


def generate_fixture(
    input_document: Mapping[str, Any], environment_manifest: Mapping[str, Any]
) -> dict[str, Any]:
    """Generate a deterministic synthetic-only oracle output document."""

    _require_exact_keys(
        input_document,
        {"schemaVersion", "fixtureClassification", "cases"},
        "document",
    )
    if input_document["schemaVersion"] != INPUT_SCHEMA_VERSION:
        raise InputValidationError(
            "INVALID_SCHEMA_VERSION",
            "schemaVersion",
            f"Schema version must be {INPUT_SCHEMA_VERSION}.",
        )
    if input_document["fixtureClassification"] != "SYNTHETIC_ONLY":
        raise InputValidationError(
            "INVALID_FIXTURE_CLASSIFICATION",
            "fixtureClassification",
            "Fixture classification must be SYNTHETIC_ONLY.",
        )
    cases = input_document["cases"]
    if not isinstance(cases, list) or not 1 <= len(cases) <= 3:
        raise InputValidationError(
            "INVALID_CASE_COUNT", "cases", "Provide between one and three cases."
        )

    environment = _environment_evidence(environment_manifest)
    outputs: list[dict[str, Any]] = []
    environment_warnings: list[dict[str, str]]
    with (
        tempfile.TemporaryDirectory(prefix="ufuq-astropy-cache-") as cache,
        set_temp_cache(cache),
        iers.conf.set_temp("auto_download", False),
        iers.conf.set_temp("iers_degraded_accuracy", "error"),
        data_conf.set_temp("allow_internet", False),
        network_blocked(),
        warnings.catch_warnings(record=True) as caught_environment,
    ):
        warnings.simplefilter("always")
        leap_seconds = iers.LeapSeconds.open(
            astropy_iers_data.IERS_LEAP_SECOND_FILE
        )
        leap_seconds.update_erfa_leap_seconds(initialize_erfa="empty")
        earth_table = iers.IERS_A.open(astropy_iers_data.IERS_A_FILE)
        with iers.earth_orientation_table.set(earth_table):
            for case in cases:
                try:
                    if not isinstance(case, Mapping):
                        raise InputValidationError(
                            "INVALID_STRUCTURE", "case", "Case must be an object."
                        )
                    _validate_case(case)
                    outputs.append(
                        _valid_case_result(case, str(environment["sha256"]))
                    )
                except InputValidationError as error:
                    if (
                        isinstance(case, Mapping)
                        and case.get("caseType") == "INVALID_INPUT"
                    ):
                        outputs.append(_invalid_case_result(case, error))
                    else:
                        raise
        environment_warnings = _warning_records(caught_environment)

    return {
        "schemaVersion": OUTPUT_SCHEMA_VERSION,
        "fixtureClassification": "SYNTHETIC_ONLY",
        "claimScope": "ENVIRONMENT_AND_ORACLE_PATH_SMOKE_ONLY",
        "generator": {
            "name": GENERATOR_NAME,
            "version": GENERATOR_VERSION,
        },
        "conventions": {
            "inputFrame": "ICRS",
            "referenceEpochRole": "EXPLICIT_METADATA_NO_SPACE_MOTION",
            "outputFrame": "AltAz",
            "altitudeUnit": "degree",
            "azimuthUnit": "degree",
            "azimuthOrigin": "GEOGRAPHIC_TRUE_NORTH",
            "azimuthPositiveDirection": "EASTWARD_CLOCKWISE",
            "observerDatum": "WGS84",
            "longitudeSign": "EAST_POSITIVE",
            "heightType": "ELLIPSOIDAL",
            "inputTimeScale": "UTC",
            "pressureHpa": 0,
            "coordinateState": "GEOMETRIC_TOPOCENTRIC",
            "toleranceStatus": "NOT_ESTABLISHED",
        },
        "networkPolicy": {
            "astropyAutoDownload": False,
            "astropyAllowInternet": False,
            "socketConnectionsBlocked": True,
            "cacheIsolation": "FRESH_TEMPORARY_CACHE",
        },
        "serializationPolicy": {
            "encoding": "UTF-8",
            "newline": "LF",
            "objectKeys": "LEXICOGRAPHIC",
            "separators": "COMPACT",
            "floatingPoint": "CPYTHON_3_14_SHORTEST_ROUND_TRIP",
            "volatileMetadataExcluded": True,
        },
        "environmentEvidence": environment,
        "environmentWarnings": environment_warnings,
        "cases": outputs,
    }
