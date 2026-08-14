"""Synthetic-only Milestone 2C.5B Batch 01 experiment runner.

This module is an offline reference/evidence tool. It imports no UFUQ production
package, accepts no catalogue input, and cannot select a production algorithm or a
scientific tolerance.
"""

from __future__ import annotations

import importlib.metadata
import math
import platform
import re
import tempfile
import warnings
from collections.abc import Callable, Mapping
from contextlib import ExitStack
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import astropy.units as u
import astropy_iers_data
import erfa
from astropy.config.paths import set_temp_cache
from astropy.coordinates import Distance, EarthLocation, SkyCoord
from astropy.time import Time
from astropy.utils import iers
from astropy.utils.data import conf as data_conf

from .experiment_protocol import (
    ProtocolValidationError,
    assert_ordered_unique,
    canonical_experiment_bytes,
    read_json_strict,
    sha256_bytes,
    sha256_file,
    validate_instance,
    validate_schema_contract,
)
from .oracle import build_environment_manifest, network_blocked


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
EXPERIMENT_ROOT = PROJECT_ROOT / "experiments"
FIXTURE_ROOT = EXPERIMENT_ROOT / "fixtures" / "batch-01"
RESULT_ROOT = EXPERIMENT_ROOT / "results" / "batch-01"
PROTOCOL_PATH = (
    REPOSITORY_ROOT
    / "docs"
    / "spikes"
    / "PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md"
)
REGISTRY_PATH = EXPERIMENT_ROOT / "experiment-registry.v1.json"
REGISTRY_SCHEMA_PATH = EXPERIMENT_ROOT / "experiment-registry.v1.schema.json"
FIXTURE_SCHEMA_PATH = EXPERIMENT_ROOT / "experiment-fixture.v1.schema.json"
RESULT_SCHEMA_PATH = EXPERIMENT_ROOT / "experiment-result.v1.schema.json"
ENVIRONMENT_PATH = PROJECT_ROOT / "environment-manifest.json"
LOCK_PATH = PROJECT_ROOT / "uv.lock"

BATCH_ID = "2C.5B-BATCH-01"
RUNNER_ID = "ufuq-astronomy-batch-01"
RUNNER_VERSION = "2C.5B-BATCH-01-v1"
RESULT_CLASSIFICATION = "SYNTHETIC_EXPERIMENT_EVIDENCE_ONLY"
SOURCE_PROHIBITIONS = {
    "catalogueSourceBytesAbsent": True,
    "hipSourceDerivedValuesAbsent": True,
    "i311EpochResolutionClaimAbsent": True,
    "i311RowsAbsent": True,
    "productionGeneratedValuesAbsent": True,
}
DECISION_LIMITS = [
    "Synthetic evidence does not establish the source meaning of I/311 Ep=1991.25.",
    "Same-family ERFA/SOFA agreement is not independent scientific validation.",
    "No Batch 01 result approves a TypeScript production implementation or policy.",
    "No numerical measurement has an AST-006 acceptance threshold.",
]


@dataclass(frozen=True)
class CheckSpec:
    check_id: str
    kind: str
    basis_classification: str


@dataclass(frozen=True)
class BatchSpec:
    experiment_id: str
    case_id: str
    group_id: str
    scope_id: str
    partitions: tuple[str, ...]
    comparison_lineage: str
    acceptance_mode: str
    checks: tuple[CheckSpec, ...]
    handler: str
    uses_leap_seconds: bool = False
    uses_iers_table: bool = False

    @property
    def fixture_id(self) -> str:
        return f"{self.experiment_id}:{self.case_id}"

    @property
    def fixture_filename(self) -> str:
        return f"{self.experiment_id.lower().replace('.', '-')}--{self.case_id}.fixture.v1.json"

    @property
    def result_filename(self) -> str:
        return f"{self.experiment_id.lower().replace('.', '-')}--{self.case_id}.result.v1.json"


def _exact(check_id: str, basis: str = "PROJECT_DECISION") -> CheckSpec:
    return CheckSpec(check_id, "EXACT_INVARIANT", basis)


def _measured(check_id: str) -> CheckSpec:
    return CheckSpec(check_id, "MEASUREMENT_ONLY", "MEASUREMENT_PROTOCOL")


BATCH_SPECS = (
    BatchSpec(
        "2C.1-EXP-01",
        "tt-tdb-utc-label-sensitivity",
        "EPOCH_LABEL_GUARDS",
        "2C.1-EXP-01-BATCH01-SYNTHETIC",
        ("TT_TDB_UTC_LABEL_SENSITIVITY",),
        "SAME_ERFA_SOFA_FAMILY",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("explicit-scale-labels-preserved"),
            _measured("scale-label-sensitivity-measured"),
            _exact("source-meaning-claim-absent"),
        ),
        "_experiment_2c1_01",
        uses_leap_seconds=True,
    ),
    BatchSpec(
        "2C.1-EXP-02",
        "calendar-decimal-year-vs-julian-epoch",
        "EPOCH_LABEL_GUARDS",
        "2C.1-EXP-02-BATCH01-SYNTHETIC",
        ("CALENDAR_DECIMAL_YEAR_VS_JULIAN_EPOCH",),
        "SAME_ERFA_SOFA_FAMILY",
        "MEASUREMENT_ONLY",
        (_measured("calendar-vs-julian-differences-measured"),),
        "_experiment_2c1_02",
        uses_leap_seconds=True,
    ),
    BatchSpec(
        "2C.1-EXP-03",
        "besselian-rejection-guard",
        "EPOCH_LABEL_GUARDS",
        "2C.1-EXP-03-BATCH01-SYNTHETIC",
        ("BESSELIAN_REJECTION_GUARD",),
        "STRUCTURAL_INVARIANT",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("besselian-source-candidate-rejected"),
            _measured("besselian-diagnostic-difference-measured"),
        ),
        "_experiment_2c1_03",
        uses_leap_seconds=True,
    ),
    BatchSpec(
        "2C.2-EXP-01",
        "decomposed-vs-composed-route",
        "ROUTE_AND_CONVENTION_CONSISTENCY",
        "2C.2-EXP-01-BATCH01-SYNTHETIC",
        ("DECOMPOSED_VS_COMPOSED_IDENTICAL_SYNTHETIC_INPUTS",),
        "SAME_ERFA_SOFA_FAMILY",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("geometric-pressure-zero-preserved"),
            _measured("route-residuals-measured-without-acceptance"),
            _exact("same-family-lineage-preserved", "SOURCE_SUPPORTED_FACT"),
            _exact("sofa-statuses-preserved", "SOURCE_SUPPORTED_FACT"),
        ),
        "_experiment_2c2_01",
        uses_leap_seconds=True,
    ),
    BatchSpec(
        "2C.2-EXP-04",
        "synthetic-convention-guards",
        "MOTION_CONVENTION_GUARDS",
        "2C.2-EXP-04-BATCH01-SYNTHETIC-CONVENTION-GUARDS",
        (
            "OMITTED_COSINE_GUARD",
            "DOUBLE_COSINE_GUARD",
            "DECLARED_TARGET_EPOCH_LABEL_GUARD",
            "TWO_PART_JD_SPLIT_INVARIANT",
            "WARNING_STATUS_PRESERVATION",
        ),
        "SAME_ERFA_SOFA_FAMILY",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("declared-target-epoch-label-preserved"),
            _exact("double-cosine-mutation-rejected"),
            _measured("guard-consequences-measured-without-acceptance"),
            _exact("omitted-cosine-mutation-rejected"),
            _exact("pmsafe-warning-status-preserved", "SOURCE_SUPPORTED_FACT"),
            _exact("two-part-jd-declarations-equivalent"),
        ),
        "_experiment_2c2_04",
    ),
    BatchSpec(
        "2C.3-EXP-01",
        "two-run-canonical-replay",
        "DETERMINISTIC_REPLAY",
        "2C.3-EXP-01-BATCH01-SYNTHETIC",
        ("TWO_RUN_CANONICAL_REPLAY", "FRESH_ISOLATED_ENVIRONMENT_REPLAY"),
        "STRUCTURAL_INVARIANT",
        "EXACT_INVARIANT_ONLY",
        (
            _exact("artifact-hashes-verified"),
            _exact("canonical-replay-bytes-identical"),
            _exact("network-and-cache-policy-preserved"),
        ),
        "_experiment_2c3_01",
        uses_leap_seconds=True,
        uses_iers_table=True,
    ),
    BatchSpec(
        "2C.4-EXP-05",
        "below-horizon-state-preservation",
        "OPTIONAL_STATE_GUARDS",
        "2C.4-EXP-05-BATCH01-SYNTHETIC",
        ("BELOW_HORIZON_GEOMETRIC_STATE_PRESERVATION",),
        "STRUCTURAL_INVARIANT",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("below-horizon-attaches-to-geometric-state"),
            _exact("optional-failure-does-not-erase-geometric-state"),
            _measured("retained-coordinate-residuals-recorded"),
            _exact("signed-altitude-azimuth-provenance-preserved"),
            _exact("warnings-and-statuses-preserved"),
        ),
        "_experiment_2c4_05",
    ),
    BatchSpec(
        "2C.4-EXP-06",
        "no-default-atmosphere",
        "OPTIONAL_STATE_GUARDS",
        "2C.4-EXP-06-BATCH01-SYNTHETIC",
        ("NO_DEFAULT_ATMOSPHERE_GUARD",),
        "SAME_ERFA_SOFA_FAMILY",
        "EXACT_INVARIANT_AND_MEASUREMENT",
        (
            _exact("missing-meteorology-produces-unavailable"),
            _exact("no-atmosphere-default-inserted"),
            _exact("not-requested-distinct-from-unavailable"),
        ),
        "_experiment_2c4_06",
    ),
    BatchSpec(
        "2C.4-EXP-07",
        "visibility-component-independence",
        "OPTIONAL_STATE_GUARDS",
        "2C.4-EXP-07-BATCH01-SYNTHETIC",
        ("VISIBILITY_COMPONENT_INDEPENDENCE",),
        "STRUCTURAL_INVARIANT",
        "EXACT_INVARIANT_ONLY",
        (
            _exact("aggregate-visibility-claim-absent"),
            _exact("geometric-state-retained-through-visibility-failure"),
            _exact("nine-visibility-components-independent"),
        ),
        "_experiment_2c4_07",
    ),
)

SPEC_BY_ID = {spec.experiment_id: spec for spec in BATCH_SPECS}
if len(SPEC_BY_ID) != len(BATCH_SPECS):
    raise RuntimeError("Duplicate Batch 01 experiment ID in compiled allowlist.")

EXPECTED_FIXTURE_SHA256 = {
    "2C.1-EXP-01": "6490f374d5eb79cb82475f6da66d491e17948c2363d79aba0438a9c67c8be338",
    "2C.1-EXP-02": "ccc6098c66c553465a4df389328f26787a117a5d578da3b35545ee476147b029",
    "2C.1-EXP-03": "09f4fc8feac68573afde57f7a14131f6e7fb4a8bf36c2a8caecd59f48a9be28d",
    "2C.2-EXP-01": "5068402b4fcbd7e4ec4a6937dc7c92122ffa4f3ed1db4ea57d57b4e2e7733e37",
    "2C.2-EXP-04": "250d17cb42b48c2b2cc74a11b88630baa634d21d22ee1851e124cb51e3130802",
    "2C.3-EXP-01": "9e5bba67fd68fe65f3788a1711f9cd90e1bed603399f35547bfa1473dcee7ad8",
    "2C.4-EXP-05": "b5104ce6df9d0cdfe029cbb234b7fa1802baa8e1517c23553c6d33ee3818cbfc",
    "2C.4-EXP-06": "477372f3226acf81af2b28dd7c896c61e866d2c0db790ee304cad4fd6c1e16d1",
    "2C.4-EXP-07": "3296d83f6068fd4c5dd90827a0a5c4711b84c4a574abb9275c2c668b10081517",
}


def _input(fixture: Mapping[str, Any], name: str) -> Any:
    return fixture["inputs"][name]["value"]


def _measurement(
    measurement_id: str, metric: str, unit: str, value: Any
) -> dict[str, Any]:
    return {
        "acceptanceStatus": "MEASURED_NO_ACCEPTANCE",
        "measurementId": measurement_id,
        "metric": metric,
        "unit": unit,
        "value": value,
    }


def _check(
    spec: CheckSpec, status: str, basis: str
) -> dict[str, Any]:
    return {
        "basis": basis,
        "basisClassification": spec.basis_classification,
        "checkId": spec.check_id,
        "kind": spec.kind,
        "numericalThreshold": None,
        "status": status,
    }


def _status(source: str, code: str, severity: str, message: str) -> dict[str, Any]:
    return {
        "code": code,
        "message": message,
        "severity": severity,
        "source": source,
    }


def _assign_status_sequence(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [dict(record, sequenceIndex=index) for index, record in enumerate(records)]


def _warning_records(caught: list[warnings.WarningMessage]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    records: list[dict[str, Any]] = []
    for warning in caught:
        identity = (warning.category.__name__, str(warning.message))
        if identity in seen:
            continue
        seen.add(identity)
        records.append(
            _status(
                "PYTHON_WARNING",
                warning.category.__name__,
                "WARNING",
                str(warning.message),
            )
        )
    return records


def _merge_warning_records(
    existing: list[dict[str, Any]], captured: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()
    for record in [*existing, *captured]:
        unsequenced = {
            key: value for key, value in record.items() if key != "sequenceIndex"
        }
        identity = (
            str(unsequenced["source"]),
            str(unsequenced["code"]),
            str(unsequenced["severity"]),
            str(unsequenced["message"]),
        )
        if identity in seen:
            continue
        seen.add(identity)
        merged.append(unsequenced)
    return _assign_status_sequence(merged)


def _angle_separation(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    left = (
        math.cos(dec1) * math.cos(ra1),
        math.cos(dec1) * math.sin(ra1),
        math.sin(dec1),
    )
    right = (
        math.cos(dec2) * math.cos(ra2),
        math.cos(dec2) * math.sin(ra2),
        math.sin(dec2),
    )
    cross = (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )
    return math.atan2(
        math.sqrt(sum(component * component for component in cross)),
        sum(a * b for a, b in zip(left, right, strict=True)),
    )


def _wrapped_difference(left: float, right: float) -> float:
    return abs(math.atan2(math.sin(left - right), math.cos(left - right)))


def _horizontal_separation(
    az1: float, alt1: float, az2: float, alt2: float
) -> float:
    return _angle_separation(az1, alt1, az2, alt2)


def _pmsafe(
    ra: float,
    dec: float,
    pm_ra_cos_dec_mas_per_year: float,
    pm_dec_mas_per_year: float,
    parallax_arcsec: float,
    radial_velocity_km_s: float,
    start: Time,
    target: Time,
    *,
    ra_rate_mode: str = "CORRECT_STARRED_ALPHA",
    start_split: tuple[float, float] | None = None,
    target_split: tuple[float, float] | None = None,
) -> tuple[tuple[float, float, float, float, float, float], int]:
    starred_rate = pm_ra_cos_dec_mas_per_year * erfa.DMAS2R
    cosine = math.cos(dec)
    modes = {
        "CORRECT_STARRED_ALPHA": starred_rate / cosine,
        "OMITTED_COSINE": starred_rate,
        "DOUBLE_COSINE": starred_rate / (cosine * cosine),
    }
    if ra_rate_mode not in modes:
        raise ProtocolValidationError(f"Unknown proper-motion guard mode {ra_rate_mode}.")
    ep1 = start_split or (float(start.tdb.jd1), float(start.tdb.jd2))
    ep2 = target_split or (float(target.tdb.jd1), float(target.tdb.jd2))
    raw = erfa.ufunc.pmsafe(
        ra,
        dec,
        modes[ra_rate_mode],
        pm_dec_mas_per_year * erfa.DMAS2R,
        parallax_arcsec,
        radial_velocity_km_s,
        ep1[0],
        ep1[1],
        ep2[0],
        ep2[1],
    )
    return tuple(float(value) for value in raw[:6]), int(raw[6])


def _guard_ra_rate_adapter_mode(mode: str) -> None:
    """Permit only one removal of cosine from starred-alpha proper motion."""

    if mode != "REMOVE_STARRED_ALPHA_COSINE_ONCE":
        raise ProtocolValidationError(f"Rejected synthetic RA-rate adapter mode: {mode}.")


def _astropy_propagate(
    ra: float,
    dec: float,
    pm_ra_cos_dec_mas_per_year: float,
    pm_dec_mas_per_year: float,
    parallax_arcsec: float,
    radial_velocity_km_s: float,
    start: Time,
    target: Time,
) -> tuple[float, float]:
    coordinate = SkyCoord(
        ra=ra * u.rad,
        dec=dec * u.rad,
        distance=Distance(parallax=parallax_arcsec * u.arcsec),
        pm_ra_cosdec=pm_ra_cos_dec_mas_per_year * u.mas / u.yr,
        pm_dec=pm_dec_mas_per_year * u.mas / u.yr,
        radial_velocity=radial_velocity_km_s * u.km / u.s,
        obstime=start,
        frame="icrs",
    )
    propagated = coordinate.apply_space_motion(new_obstime=target)
    return float(propagated.ra.rad), float(propagated.dec.rad)


def _common_astrometry(fixture: Mapping[str, Any]) -> tuple[float, ...]:
    return (
        float(_input(fixture, "rightAscensionRad")),
        math.radians(float(_input(fixture, "declinationDeg"))),
        float(_input(fixture, "properMotionRaCosDecMasPerYear")),
        float(_input(fixture, "properMotionDecMasPerYear")),
        float(_input(fixture, "parallaxArcsec")),
        float(_input(fixture, "radialVelocityKmPerSecond")),
    )


def _tdb_reference_location(fixture: Mapping[str, Any]) -> EarthLocation:
    values = tuple(
        float(value)
        for value in _input(fixture, "tdbConversionLocationGeocentricMetres")
    )
    if values != (0.0, 0.0, 0.0):
        raise ProtocolValidationError(
            "Batch 01 epoch-label experiments require the explicit synthetic geocentre."
        )
    return EarthLocation.from_geocentric(*values, unit=u.m)


def _experiment_2c1_01(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    ra, dec, pmra, pmdec, parallax, rv = _common_astrometry(fixture)
    tdb_location = _tdb_reference_location(fixture)
    epoch_value = float(_input(fixture, "sourceEpochNumericLabel"))
    target = Time(
        float(_input(fixture, "targetEpochNumericLabel")),
        format="jyear",
        scale="tdb",
        location=tdb_location,
    )
    starts = {
        scale: Time(
            epoch_value,
            format="jyear",
            scale=scale,
            location=tdb_location,
        )
        for scale in ("tt", "tdb", "utc")
    }
    direct: dict[str, tuple[float, float]] = {}
    astropy: dict[str, tuple[float, float]] = {}
    statuses: list[dict[str, Any]] = [
        _status(
            "ASTROPY_TIME",
            "SYNTHETIC_GEOCENTRE_LOCATION_EXPLICIT",
            "INFO",
            "TDB/TT conversion uses the declared ITRS geocentric [0,0,0] metre location.",
        )
    ]
    for scale, start in starts.items():
        output, status = _pmsafe(
            ra, dec, pmra, pmdec, parallax, rv, start, target
        )
        direct[scale] = (output[0], output[1])
        astropy[scale] = _astropy_propagate(
            ra, dec, pmra, pmdec, parallax, rv, start, target
        )
        statuses.append(
            _status(
                "ERFA_PMSAFE",
                f"PMSAFE_STATUS_{status}_{scale.upper()}",
                "INFO" if status == 0 else "WARNING",
                f"Synthetic {scale.upper()} label returned raw pmsafe status {status}.",
            )
        )

    measurements: list[dict[str, Any]] = []
    for left, right in (("tt", "tdb"), ("tt", "utc"), ("tdb", "utc")):
        measurements.extend(
            [
                _measurement(
                    f"{left}-{right}-start-instant-seconds",
                    "COMPONENT_RESIDUAL",
                    "SECOND",
                    float((starts[left].tdb - starts[right].tdb).to_value(u.s)),
                ),
                _measurement(
                    f"{left}-{right}-propagated-separation",
                    "GREAT_CIRCLE_ANGULAR_SEPARATION",
                    "RADIAN",
                    _angle_separation(*direct[left], *direct[right]),
                ),
            ]
        )
    for scale in ("tt", "tdb", "utc"):
        measurements.append(
            _measurement(
                f"{scale}-astropy-vs-pyerfa-separation",
                "GREAT_CIRCLE_ANGULAR_SEPARATION",
                "RADIAN",
                _angle_separation(*astropy[scale], *direct[scale]),
            )
        )

    checks = {
        "explicit-scale-labels-preserved": (
            set(starts) == {"tt", "tdb", "utc"}
            and tuple(
                _input(fixture, "tdbConversionLocationGeocentricMetres")
            )
            == (0, 0, 0),
            (
                "The fixture's three explicit Julian-epoch scale labels remained "
                "distinct inputs with an explicit synthetic geocentre conversion location."
            ),
        ),
        "scale-label-sensitivity-measured": (
            True,
            "Instant and propagated-direction differences were recorded without acceptance.",
        ),
        "source-meaning-claim-absent": (
            fixture["sourceProhibitions"]["i311EpochResolutionClaimAbsent"] is True,
            "The synthetic comparison carries no claim about the source epoch time scale.",
        ),
    }
    return _evidence_from_checks(spec, measurements, [], statuses, checks)


def _experiment_2c1_02(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    ra, dec, pmra, pmdec, parallax, rv = _common_astrometry(fixture)
    tdb_location = _tdb_reference_location(fixture)
    target = Time(
        float(_input(fixture, "targetEpochNumericLabel")),
        format="jyear",
        scale="tdb",
        location=tdb_location,
    )
    labels = [float(value) for value in _input(fixture, "comparisonYearLabels")]
    measurements: list[dict[str, Any]] = []
    for label in labels:
        julian = Time(
            label, format="jyear", scale="tt", location=tdb_location
        )
        calendar = Time(
            label, format="decimalyear", scale="tt", location=tdb_location
        )
        julian_output = _astropy_propagate(
            ra, dec, pmra, pmdec, parallax, rv, julian, target
        )
        calendar_output = _astropy_propagate(
            ra, dec, pmra, pmdec, parallax, rv, calendar, target
        )
        case = str(label).replace(".", "-")
        measurements.extend(
            [
                _measurement(
                    f"label-{case}-start-instant-seconds",
                    "COMPONENT_RESIDUAL",
                    "SECOND",
                    float((julian.tdb - calendar.tdb).to_value(u.s)),
                ),
                _measurement(
                    f"label-{case}-propagated-separation",
                    "GREAT_CIRCLE_ANGULAR_SEPARATION",
                    "RADIAN",
                    _angle_separation(*julian_output, *calendar_output),
                ),
            ]
        )
    checks = {
        "calendar-vs-julian-differences-measured": (
            True,
            "Calendar decimal-year and Julian-epoch differences were measured only; no threshold exists.",
        )
    }
    statuses = [
        _status(
            "ASTROPY_TIME",
            "SYNTHETIC_GEOCENTRE_LOCATION_EXPLICIT",
            "INFO",
            "TDB/TT conversion uses the declared ITRS geocentric [0,0,0] metre location.",
        ),
        _status(
            "BATCH01_EPOCH_PROTOCOL",
            "CALENDAR_DECIMAL_YEAR_DIAGNOSTIC_ONLY",
            "INFO",
            "Calendar decimal year remains a labelled diagnostic, not a source interpretation.",
        )
    ]
    return _evidence_from_checks(spec, measurements, [], statuses, checks)


def _experiment_2c1_03(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    ra, dec, pmra, pmdec, parallax, rv = _common_astrometry(fixture)
    tdb_location = _tdb_reference_location(fixture)
    label = float(_input(fixture, "sourceEpochNumericLabel"))
    target = Time(
        float(_input(fixture, "targetEpochNumericLabel")),
        format="jyear",
        scale="tdb",
        location=tdb_location,
    )
    julian = Time(label, format="jyear", scale="tt", location=tdb_location)
    besselian = Time(
        label, format="byear", scale="tt", location=tdb_location
    )
    julian_output, julian_status = _pmsafe(
        ra, dec, pmra, pmdec, parallax, rv, julian, target
    )
    besselian_output, besselian_status = _pmsafe(
        ra, dec, pmra, pmdec, parallax, rv, besselian, target
    )
    candidate_allowlist = tuple(_input(fixture, "sourceCandidateRepresentationAllowlist"))
    rejected = str(_input(fixture, "diagnosticRejectedRepresentation"))
    measurements = [
        _measurement(
            "besselian-vs-julian-start-instant-seconds",
            "COMPONENT_RESIDUAL",
            "SECOND",
            float((besselian.tdb - julian.tdb).to_value(u.s)),
        ),
        _measurement(
            "besselian-vs-julian-propagated-separation",
            "GREAT_CIRCLE_ANGULAR_SEPARATION",
            "RADIAN",
            _angle_separation(
                julian_output[0],
                julian_output[1],
                besselian_output[0],
                besselian_output[1],
            ),
        ),
    ]
    checks = {
        "besselian-source-candidate-rejected": (
            rejected == "BYEAR" and rejected not in candidate_allowlist,
            "BYEAR was rejected by the exact source-candidate representation allowlist.",
        ),
        "besselian-diagnostic-difference-measured": (
            True,
            "The rejected representation was evaluated only to record a diagnostic difference.",
        ),
    }
    statuses = [
        _status(
            "ASTROPY_TIME",
            "SYNTHETIC_GEOCENTRE_LOCATION_EXPLICIT",
            "INFO",
            "TDB/TT conversion uses the declared ITRS geocentric [0,0,0] metre location.",
        ),
        _status(
            "BATCH01_EPOCH_GUARD",
            "BESSELIAN_REPRESENTATION_REJECTED",
            "INFO",
            "BYEAR is excluded from the source-candidate set regardless of its numerical difference.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_JULIAN_DIAGNOSTIC_STATUS_{julian_status}",
            "INFO" if julian_status == 0 else "WARNING",
            f"The Julian diagnostic pmsafe raw status {julian_status} was retained.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_BESSELIAN_DIAGNOSTIC_STATUS_{besselian_status}",
            "INFO" if besselian_status == 0 else "WARNING",
            f"The Besselian diagnostic pmsafe raw status {besselian_status} was retained.",
        ),
    ]
    return _evidence_from_checks(spec, measurements, [], statuses, checks)


def _experiment_2c2_01(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    ra, dec, pmra, pmdec, parallax, rv = _common_astrometry(fixture)
    start = Time(
        float(_input(fixture, "sourceEpochNumericLabel")),
        format="jyear",
        scale="tdb",
    )
    target = Time(2000.0, format="jyear", scale="tdb")
    propagated, pmsafe_status = _pmsafe(
        ra, dec, pmra, pmdec, parallax, rv, start, target
    )
    utc_raw = erfa.ufunc.dtf2d(
        "UTC",
        int(_input(fixture, "observationYear")),
        int(_input(fixture, "observationMonth")),
        int(_input(fixture, "observationDay")),
        int(_input(fixture, "observationHour")),
        int(_input(fixture, "observationMinute")),
        float(_input(fixture, "observationSecond")),
    )
    utc1, utc2, utc_status = float(utc_raw[0]), float(utc_raw[1]), int(utc_raw[2])
    route_inputs = (
        float(_input(fixture, "dut1Seconds")),
        float(_input(fixture, "longitudeEastRad")),
        math.radians(float(_input(fixture, "geodeticLatitudeDeg"))),
        float(_input(fixture, "ellipsoidalHeightM")),
        float(_input(fixture, "polarMotionXRad")),
        float(_input(fixture, "polarMotionYRad")),
        float(_input(fixture, "pressureHpa")),
        float(_input(fixture, "temperatureC")),
        float(_input(fixture, "relativeHumidityFraction")),
        float(_input(fixture, "wavelengthMicrometre")),
    )
    apco_raw = erfa.ufunc.apco13(utc1, utc2, *route_inputs)
    astrom, eo_decomposed, apco_status = apco_raw[0], float(apco_raw[1]), int(apco_raw[2])
    ri, di = erfa.atciq(*propagated, astrom)
    decomposed = tuple(float(value) for value in erfa.atioq(ri, di, astrom))
    composed_raw = erfa.ufunc.atco13(
        *propagated,
        utc1,
        utc2,
        *route_inputs,
    )
    composed = tuple(float(value) for value in composed_raw[:6])
    atco_status = int(composed_raw[6])
    aob_a, zob_a, hob_a, dob_a, rob_a = decomposed
    aob_b, zob_b, hob_b, dob_b, rob_b, eo_composed = composed
    alt_a = math.pi / 2.0 - zob_a
    alt_b = math.pi / 2.0 - zob_b
    measurements = [
        _measurement(
            "altitude-residual",
            "ALTITUDE_DIFFERENCE",
            "RADIAN",
            alt_a - alt_b,
        ),
        _measurement(
            "azimuth-residual",
            "WRAPPED_AZIMUTH_DIFFERENCE",
            "RADIAN",
            _wrapped_difference(aob_a, aob_b),
        ),
        _measurement(
            "horizontal-direction-separation",
            "GREAT_CIRCLE_ANGULAR_SEPARATION",
            "RADIAN",
            _horizontal_separation(aob_a, alt_a, aob_b, alt_b),
        ),
        _measurement(
            "observed-component-residuals",
            "COMPONENT_RESIDUAL",
            "RADIAN",
            [
                _wrapped_difference(hob_a, hob_b),
                dob_a - dob_b,
                _wrapped_difference(rob_a, rob_b),
                eo_decomposed - eo_composed,
            ],
        ),
    ]
    statuses = [
        _status(
            "ERFA_DTF2D",
            f"DTF2D_STATUS_{utc_status}",
            "INFO" if utc_status == 0 else "WARNING",
            f"Raw UTC encoding status {utc_status} was preserved.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_STATUS_{pmsafe_status}",
            "INFO" if pmsafe_status == 0 else "WARNING",
            f"Shared preliminary propagation status {pmsafe_status} was preserved.",
        ),
        _status(
            "ERFA_APCO13",
            f"APCO13_STATUS_{apco_status}",
            "INFO" if apco_status == 0 else "WARNING",
            f"Decomposed route status {apco_status} was preserved.",
        ),
        _status(
            "ERFA_ATCO13",
            f"ATCO13_STATUS_{atco_status}",
            "INFO" if atco_status == 0 else "WARNING",
            f"Composed route status {atco_status} was preserved.",
        ),
    ]
    checks = {
        "geometric-pressure-zero-preserved": (
            route_inputs[6] == 0.0,
            "Both candidate routes received explicit pressure zero and remained geometric.",
        ),
        "route-residuals-measured-without-acceptance": (
            True,
            "All route residuals are measurements with no numerical threshold.",
        ),
        "same-family-lineage-preserved": (
            spec.comparison_lineage == "SAME_ERFA_SOFA_FAMILY",
            "The decomposed and composed branches are labelled as shared ERFA/SOFA lineage.",
        ),
        "sofa-statuses-preserved": (
            all(isinstance(value, int) for value in (utc_status, pmsafe_status, apco_status, atco_status)),
            "Raw status integers from every status-returning ERFA stage were retained.",
        ),
    }
    return _evidence_from_checks(spec, measurements, [], statuses, checks)


def _experiment_2c2_04(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    ra, dec, pmra, pmdec, parallax, rv = _common_astrometry(fixture)
    start = Time(
        float(_input(fixture, "sourceEpochNumericLabel")),
        format="jyear",
        scale="tdb",
    )
    target = Time(
        float(_input(fixture, "targetEpochNumericLabel")),
        format="jyear",
        scale="tdb",
    )
    correct, correct_status = _pmsafe(
        ra, dec, pmra, pmdec, parallax, rv, start, target
    )
    omitted, omitted_status = _pmsafe(
        ra,
        dec,
        pmra,
        pmdec,
        parallax,
        rv,
        start,
        target,
        ra_rate_mode="OMITTED_COSINE",
    )
    doubled, doubled_status = _pmsafe(
        ra,
        dec,
        pmra,
        pmdec,
        parallax,
        rv,
        start,
        target,
        ra_rate_mode="DOUBLE_COSINE",
    )
    measurements = [
        _measurement(
            "double-cosine-propagated-separation",
            "GREAT_CIRCLE_ANGULAR_SEPARATION",
            "RADIAN",
            _angle_separation(correct[0], correct[1], doubled[0], doubled[1]),
        ),
        _measurement(
            "omitted-cosine-propagated-separation",
            "GREAT_CIRCLE_ANGULAR_SEPARATION",
            "RADIAN",
            _angle_separation(correct[0], correct[1], omitted[0], omitted[1]),
        ),
    ]

    start_flat = [
        float(value) for value in _input(fixture, "sourceEpochTdbJdSplits")
    ]
    target_flat = [
        float(value) for value in _input(fixture, "targetEpochTdbJdSplits")
    ]
    if len(start_flat) != 6 or len(target_flat) != 6:
        raise ProtocolValidationError("Batch 01 requires exactly three JD split pairs.")
    start_splits = list(zip(start_flat[::2], start_flat[1::2], strict=True))
    target_splits = list(zip(target_flat[::2], target_flat[1::2], strict=True))
    split_outputs: list[tuple[float, ...]] = []
    split_statuses: list[int] = []
    for index, (start_split, target_split) in enumerate(
        zip(start_splits, target_splits, strict=True)
    ):
        output, status = _pmsafe(
            ra,
            dec,
            pmra,
            pmdec,
            parallax,
            rv,
            start,
            target,
            start_split=start_split,
            target_split=target_split,
        )
        split_outputs.append(output)
        split_statuses.append(status)
        if index:
            measurements.append(
                _measurement(
                    f"jd-split-{index}-coordinate-residuals",
                    "COMPONENT_RESIDUAL",
                    "MIXED_PMSAFE_OUTPUT_UNITS",
                    [
                        _wrapped_difference(output[0], split_outputs[0][0]),
                        output[1] - split_outputs[0][1],
                        output[2] - split_outputs[0][2],
                        output[3] - split_outputs[0][3],
                        output[4] - split_outputs[0][4],
                        output[5] - split_outputs[0][5],
                    ],
                )
            )

    zero_parallax = float(_input(fixture, "warningParallaxArcsec"))
    warning_raw, warning_status = _pmsafe(
        ra,
        math.radians(float(_input(fixture, "warningDeclinationDeg"))),
        float(_input(fixture, "warningProperMotionRaCosDecMasPerYear")),
        float(_input(fixture, "warningProperMotionDecMasPerYear")),
        zero_parallax,
        float(_input(fixture, "warningRadialVelocityKmPerSecond")),
        start,
        target,
    )
    warning_dec = math.radians(float(_input(fixture, "warningDeclinationDeg")))
    warning_pmr = (
        float(_input(fixture, "warningProperMotionRaCosDecMasPerYear"))
        * erfa.DMAS2R
        / math.cos(warning_dec)
    )
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        wrapper = erfa.pmsafe(
            ra,
            warning_dec,
            warning_pmr,
            float(_input(fixture, "warningProperMotionDecMasPerYear"))
            * erfa.DMAS2R,
            zero_parallax,
            float(_input(fixture, "warningRadialVelocityKmPerSecond")),
            float(start.tdb.jd1),
            float(start.tdb.jd2),
            float(target.tdb.jd1),
            float(target.tdb.jd2),
        )
    wrapper_values = tuple(float(value) for value in wrapper)
    measurements.append(
        _measurement(
            "warning-wrapper-vs-raw-residuals",
            "COMPONENT_RESIDUAL",
            "MIXED_PMSAFE_OUTPUT_UNITS",
            [
                _wrapped_difference(wrapper_values[0], warning_raw[0]),
                wrapper_values[1] - warning_raw[1],
                wrapper_values[2] - warning_raw[2],
                wrapper_values[3] - warning_raw[3],
                wrapper_values[4] - warning_raw[4],
                wrapper_values[5] - warning_raw[5],
            ],
        )
    )
    caught_records = _warning_records(caught)
    statuses = [
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_CORRECT_RATE_STATUS_{correct_status}",
            "INFO" if correct_status == 0 else "WARNING",
            f"The correct starred-alpha conversion raw status {correct_status} was retained.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_OMITTED_COSINE_STATUS_{omitted_status}",
            "INFO" if omitted_status == 0 else "WARNING",
            f"The omitted-cosine diagnostic raw status {omitted_status} was retained.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_DOUBLE_COSINE_STATUS_{doubled_status}",
            "INFO" if doubled_status == 0 else "WARNING",
            f"The double-cosine diagnostic raw status {doubled_status} was retained.",
        ),
        _status(
            "ERFA_PMSAFE",
            f"PMSAFE_WARNING_STATUS_{warning_status}",
            "WARNING" if warning_status else "INFO",
            f"Raw warning-producing pmsafe status {warning_status} was retained.",
        ),
        *[
            _status(
                "ERFA_PMSAFE_SPLIT",
                f"PMSAFE_SPLIT_{index}_STATUS_{status}",
                "INFO" if status == 0 else "WARNING",
                f"Two-part-JD split {index} raw status {status} was retained.",
            )
            for index, status in enumerate(split_statuses)
        ],
    ]
    source_epoch_jd = 2448349.0625
    target_epoch_jd = 2451545.0
    splits_equivalent = (
        len(start_splits) == len(target_splits) == 3
        and all(sum(pair) == source_epoch_jd for pair in start_splits)
        and all(sum(pair) == target_epoch_jd for pair in target_splits)
    )
    _guard_ra_rate_adapter_mode("REMOVE_STARRED_ALPHA_COSINE_ONCE")
    rejected_modes = tuple(_input(fixture, "rejectedRaRateModes"))

    def rejects_rate_mode(mode: str) -> bool:
        try:
            _guard_ra_rate_adapter_mode(mode)
        except ProtocolValidationError:
            return True
        return False

    checks = {
        "declared-target-epoch-label-preserved": (
            _input(fixture, "declaredTargetEpochLabel") == "J2000.0"
            and _input(fixture, "declaredTargetTimeScale") == "TDB"
            and _input(fixture, "outputFrameAfterPropagation") == "ICRS"
            and float(_input(fixture, "sourceEpochNumericLabel")) == 1991.25
            and float(_input(fixture, "targetEpochNumericLabel")) == 2000.0
            and float(start.tdb.jd1) + float(start.tdb.jd2) == source_epoch_jd
            and float(target.tdb.jd1) + float(target.tdb.jd2) == target_epoch_jd,
            "The propagated state retains ICRS and explicitly declares J2000.0 TDB as an epoch interface.",
        ),
        "double-cosine-mutation-rejected": (
            rejected_modes == ("OMITTED_COSINE", "DOUBLE_COSINE")
            and rejects_rate_mode("DOUBLE_COSINE"),
            "The deliberately injected double-cosine adapter mode is rejected structurally.",
        ),
        "guard-consequences-measured-without-acceptance": (
            True,
            "Cosine, JD-split, and wrapper residuals are recorded without thresholds.",
        ),
        "omitted-cosine-mutation-rejected": (
            rejected_modes == ("OMITTED_COSINE", "DOUBLE_COSINE")
            and rejects_rate_mode("OMITTED_COSINE"),
            "The deliberately injected omitted-cosine adapter mode is rejected structurally.",
        ),
        "pmsafe-warning-status-preserved": (
            warning_status == 1
            and any(record["code"] == "ErfaWarning" for record in caught_records),
            "Raw pmsafe status 1 and the public-wrapper ErfaWarning were both retained.",
        ),
        "two-part-jd-declarations-equivalent": (
            splits_equivalent,
            "All declared two-part splits encode the same exact binary-rational source and target JDs.",
        ),
    }
    return _evidence_from_checks(
        spec, measurements, caught_records, statuses, checks
    )


def _experiment_2c3_01(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    payload = {
        "fixtureId": fixture["fixtureId"],
        "tokens": list(_input(fixture, "replayPayloadTokens")),
    }
    first = canonical_experiment_bytes(payload)
    second = canonical_experiment_bytes(payload)
    used = {record["artifactId"]: record for record in fixture["usedArtifactHashes"]}
    earth_path = Path(astropy_iers_data.IERS_A_FILE)
    leap_path = Path(astropy_iers_data.IERS_LEAP_SECOND_FILE)
    actual = {
        "astropy-iers-data/finals2000A.all": sha256_file(earth_path),
        "astropy-iers-data/Leap_Second.dat": sha256_file(leap_path),
    }
    artifacts_match = set(used) == set(actual) and all(
        used[artifact_id]["sha256"] == digest
        for artifact_id, digest in actual.items()
    )
    measurements = [
        _measurement(
            "canonical-payload-byte-length",
            "DETERMINISTIC_BYTE_LENGTH",
            "BYTE",
            len(first),
        ),
        _measurement(
            "canonical-payload-sha256",
            "DETERMINISTIC_SHA256",
            "SHA256_HEX",
            sha256_bytes(first),
        ),
    ]
    checks = {
        "artifact-hashes-verified": (
            artifacts_match,
            "The two consumed smoke-only astropy-iers-data files match fixture hashes.",
        ),
        "canonical-replay-bytes-identical": (
            first == second and sha256_bytes(first) == sha256_bytes(second),
            "Repeated canonical evidence-payload bytes and SHA-256 are identical.",
        ),
        "network-and-cache-policy-preserved": (
            True,
            "Execution occurred with network blocked, auto-download disabled, and a fresh cache context.",
        ),
    }
    statuses = [
        _status(
            "BATCH01_REPLAY",
            "BYTE_IDENTITY_DETERMINISM_ONLY",
            "INFO",
            "Byte identity establishes deterministic replay only, not scientific correctness.",
        )
    ]
    return _evidence_from_checks(spec, measurements, [], statuses, checks)


def _classify_geometric_horizon(
    geometric: Mapping[str, Any], prior_statuses: list[str]
) -> dict[str, Any]:
    altitude = float(geometric["geometricAltitudeDeg"])
    horizon = "BELOW_GEOMETRIC_HORIZON" if altitude < 0.0 else "AT_OR_ABOVE_GEOMETRIC_HORIZON"
    return {
        "geometricDirection": dict(geometric),
        "horizonClassification": horizon,
        "statuses": list(prior_statuses) + [horizon],
    }


def _experiment_2c4_05(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    geometric = {
        "azimuthDeg": float(_input(fixture, "geometricAzimuthDeg")),
        "frame": "GEOMETRIC_HORIZONTAL",
        "geometricAltitudeDeg": float(_input(fixture, "geometricAltitudeDeg")),
        "provenance": str(_input(fixture, "geometricProvenance")),
    }
    prior_statuses = list(_input(fixture, "earlierStructuredStatuses"))
    prior_warnings = list(_input(fixture, "earlierWarnings"))
    classified = _classify_geometric_horizon(geometric, prior_statuses)
    optional_failure = {
        "geometricDirection": classified["geometricDirection"],
        "optionalOutcome": "VISIBILITY_POLICY_UNAVAILABLE",
        "statuses": classified["statuses"] + ["VISIBILITY_POLICY_UNAVAILABLE"],
    }
    retained = optional_failure["geometricDirection"]
    measurements = [
        _measurement(
            "retained-coordinate-residuals",
            "COMPONENT_RESIDUAL",
            "DEGREE",
            [
                retained["azimuthDeg"] - geometric["azimuthDeg"],
                retained["geometricAltitudeDeg"] - geometric["geometricAltitudeDeg"],
            ],
        )
    ]
    checks = {
        "below-horizon-attaches-to-geometric-state": (
            classified["horizonClassification"] == "BELOW_GEOMETRIC_HORIZON"
            and "geometricDirection" in classified,
            "Below-horizon is attached to, rather than substituted for, the valid geometric state.",
        ),
        "optional-failure-does-not-erase-geometric-state": (
            optional_failure["geometricDirection"] == geometric,
            "A later visibility non-result retains the earlier geometric state.",
        ),
        "retained-coordinate-residuals-recorded": (
            True,
            "Retained-coordinate residuals were recorded without a numerical acceptance threshold.",
        ),
        "signed-altitude-azimuth-provenance-preserved": (
            retained == geometric and retained["geometricAltitudeDeg"] < 0.0,
            "Signed altitude, defined azimuth, frame, and provenance were preserved exactly.",
        ),
        "warnings-and-statuses-preserved": (
            classified["statuses"][: len(prior_statuses)] == prior_statuses
            and prior_warnings == list(_input(fixture, "earlierWarnings")),
            "Earlier synthetic warnings and statuses remain ahead of the horizon classification.",
        ),
    }
    warnings_out = [
        _status("SYNTHETIC_UPSTREAM", code, "WARNING", f"Preserved upstream warning: {code}.")
        for code in prior_warnings
    ]
    statuses = [
        *[
            _status("SYNTHETIC_UPSTREAM", code, "INFO", f"Preserved upstream status: {code}.")
            for code in prior_statuses
        ],
        _status(
            "GEOMETRIC_HORIZON",
            classified["horizonClassification"],
            "INFO",
            (
                "The valid geometric direction was retained with signed altitude "
                f"{geometric['geometricAltitudeDeg']} degree and azimuth {geometric['azimuthDeg']} degree."
            ),
        ),
        _status(
            "OPTIONAL_VISIBILITY_STAGE",
            optional_failure["optionalOutcome"],
            "INFO",
            "The later optional-stage non-result did not erase the geometric direction.",
        ),
    ]
    return _evidence_from_checks(spec, measurements, warnings_out, statuses, checks)


def _evaluate_refraction_request(requested: bool, meteorology: Any) -> dict[str, Any]:
    if not requested:
        return {"atmosphereInputs": {}, "state": "REFRACTION_NOT_REQUESTED"}
    if meteorology == "MISSING":
        return {"atmosphereInputs": {}, "state": "REFRACTION_UNAVAILABLE"}
    return {"atmosphereInputs": meteorology, "state": "REFRACTION_INPUT_SUPPLIED_UNAPPROVED"}


def _experiment_2c4_06(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    meteorology = _input(fixture, "missingMeteorology")
    not_requested = _evaluate_refraction_request(
        bool(_input(fixture, "notRequestedBranchRequested")), meteorology
    )
    requested_missing = _evaluate_refraction_request(
        bool(_input(fixture, "requestedMissingBranchRequested")), meteorology
    )
    checks = {
        "missing-meteorology-produces-unavailable": (
            requested_missing["state"] == "REFRACTION_UNAVAILABLE",
            "Requested refraction with missing meteorology returns unavailable.",
        ),
        "no-atmosphere-default-inserted": (
            not not_requested["atmosphereInputs"]
            and not requested_missing["atmosphereInputs"],
            "Neither branch inserted pressure, temperature, humidity, wavelength, or lapse defaults.",
        ),
        "not-requested-distinct-from-unavailable": (
            not_requested["state"] == "REFRACTION_NOT_REQUESTED"
            and requested_missing["state"] == "REFRACTION_UNAVAILABLE",
            "Not-requested and requested-but-unavailable remain distinct states.",
        ),
    }
    statuses = [
        _status(
            "REFRACTION_REQUEST",
            not_requested["state"],
            "INFO",
            "The no-refraction branch supplied no atmosphere values.",
        ),
        _status(
            "REFRACTION_REQUEST",
            requested_missing["state"],
            "INFO",
            "The requested branch remained unavailable without inserting defaults.",
        ),
    ]
    return _evidence_from_checks(spec, [], [], statuses, checks)


def _experiment_2c4_07(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    component_names = list(_input(fixture, "visibilityComponentNames"))
    components = {
        name: {"state": "UNAVAILABLE", "provenance": "SYNTHETIC_EXPLICIT"}
        for name in component_names
    }
    geometric = {
        "azimuthDeg": float(_input(fixture, "geometricAzimuthDeg")),
        "geometricAltitudeDeg": float(_input(fixture, "geometricAltitudeDeg")),
        "state": "GEOMETRIC_HORIZONTAL_DIRECTION",
    }
    visibility_state = {
        "components": components,
        "geometricDirection": geometric,
        "outcome": "VISIBILITY_POLICY_UNAVAILABLE",
    }
    expected_names = set(_input(fixture, "requiredIndependentVisibilityComponents"))
    checks = {
        "aggregate-visibility-claim-absent": (
            "visible" not in visibility_state
            and "isVisible" not in visibility_state
            and "aggregateVisibility" not in visibility_state,
            "No aggregate visible/not-visible field was produced.",
        ),
        "geometric-state-retained-through-visibility-failure": (
            visibility_state["geometricDirection"] == geometric,
            "Unavailable visibility policy retains the valid geometric direction.",
        ),
        "nine-visibility-components-independent": (
            len(components) == 9 and set(components) == expected_names,
            "Exactly the nine declared visibility components remain independently keyed.",
        ),
    }
    statuses = [
        _status(
            "VISIBILITY_POLICY",
            "VISIBILITY_POLICY_UNAVAILABLE",
            "INFO",
            "Nine component states were retained without an aggregate visibility claim.",
        ),
        _status(
            "GEOMETRIC_DIRECTION",
            "GEOMETRIC_STATE_RETAINED",
            "INFO",
            (
                "Visibility unavailability retained geometric altitude "
                f"{geometric['geometricAltitudeDeg']} degree and azimuth {geometric['azimuthDeg']} degree."
            ),
        ),
    ]
    return _evidence_from_checks(spec, [], [], statuses, checks)


HANDLERS: dict[str, Callable[[BatchSpec, Mapping[str, Any]], dict[str, Any]]] = {
    name: value
    for name, value in globals().items()
    if name.startswith("_experiment_") and callable(value)
}


def _evidence_from_checks(
    spec: BatchSpec,
    measurements: list[dict[str, Any]],
    warning_records: list[dict[str, Any]],
    status_records: list[dict[str, Any]],
    check_results: Mapping[str, tuple[bool, str]],
) -> dict[str, Any]:
    expected = {check.check_id for check in spec.checks}
    if set(check_results) != expected:
        raise ProtocolValidationError(
            f"{spec.experiment_id} handler check inventory does not match its allowlist."
        )
    checks: list[dict[str, Any]] = []
    for check_spec in spec.checks:
        passed, basis = check_results[check_spec.check_id]
        if check_spec.kind == "MEASUREMENT_ONLY":
            status = "MEASURED_NO_ACCEPTANCE" if passed else "NOT_RUN"
        else:
            status = "PASS" if passed else "FAIL"
        checks.append(_check(check_spec, status, basis))
    result = {
        "checks": sorted(checks, key=lambda item: item["checkId"]),
        "measurements": sorted(
            measurements, key=lambda item: item["measurementId"]
        ),
        "structuredStatuses": _assign_status_sequence(status_records),
        "warnings": _assign_status_sequence(warning_records),
    }
    assert_ordered_unique(result["checks"], "checkId")
    assert_ordered_unique(result["measurements"], "measurementId")
    for collection in ("structuredStatuses", "warnings"):
        indexes = [record["sequenceIndex"] for record in result[collection]]
        if indexes != list(range(len(indexes))):
            raise ProtocolValidationError(
                f"{spec.experiment_id} has non-contiguous status sequence indexes."
            )
    return result


def _schema_bundle() -> dict[str, dict[str, Any]]:
    paths = {
        "fixture": FIXTURE_SCHEMA_PATH,
        "registry": REGISTRY_SCHEMA_PATH,
        "result": RESULT_SCHEMA_PATH,
    }
    schemas = {name: read_json_strict(path) for name, path in paths.items()}
    for schema in schemas.values():
        validate_schema_contract(schema)
    return schemas


def _compiled_batch_membership() -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for spec in BATCH_SPECS:
        groups.setdefault(spec.group_id, []).append(
            {
                "experimentId": spec.experiment_id,
                "includedPartitions": list(spec.partitions),
                "scopeId": spec.scope_id,
            }
        )
    return groups


def validate_registry(
    registry: Mapping[str, Any], registry_schema: Mapping[str, Any]
) -> None:
    validate_instance(registry, registry_schema)
    if registry["schemaVersion"] != "ufuq.astronomy-experiment-registry.v1":
        raise ProtocolValidationError("Unexpected experiment registry version.")
    experiments = {
        record["experimentId"]: record for record in registry["experiments"]
    }
    if len(experiments) != len(registry["experiments"]):
        raise ProtocolValidationError("Experiment registry IDs must be unique.")
    first_batch_ids = {
        record["experimentId"]
        for record in registry["experiments"]
        if record["firstBatch"]
    }
    if first_batch_ids != set(SPEC_BY_ID):
        raise ProtocolValidationError(
            "Compiled Batch 01 allowlist does not match registry firstBatch IDs."
        )
    batch = registry["firstBatch"]
    if batch["batchId"] != BATCH_ID:
        raise ProtocolValidationError("Unexpected first-batch ID.")
    if batch["status"] != "PROPOSED_SYNTHETIC_EXECUTION_ONLY":
        raise ProtocolValidationError(
            "Registry v1 no longer matches its frozen pre-execution authorization state."
        )
    if batch["inputClassification"] != "SYNTHETIC_EXPERIMENT_INPUT":
        raise ProtocolValidationError("Batch 01 must be synthetic-only.")
    if batch["prohibitedInputClasses"] != [
        "SOURCE_DERIVED",
        "PRODUCTION_GENERATED",
    ]:
        raise ProtocolValidationError("Batch prohibited input classes changed.")
    actual_groups = {
        group["groupId"]: group["members"]
        for group in batch["executionGroups"]
    }
    if actual_groups != _compiled_batch_membership():
        raise ProtocolValidationError(
            "Registry Batch 01 groups/scopes/partitions differ from compiled allowlist."
        )
    for spec in BATCH_SPECS:
        record = experiments[spec.experiment_id]
        if record["currentClassification"] != "RUNNABLE_SYNTHETIC_NOW":
            raise ProtocolValidationError(
                f"{spec.experiment_id} is no longer synthetic-runnable."
            )
        if record["comparisonLineage"] != spec.comparison_lineage:
            raise ProtocolValidationError(
                f"{spec.experiment_id} lineage differs from the allowlist."
            )
        if record["acceptanceMode"] != spec.acceptance_mode:
            raise ProtocolValidationError(
                f"{spec.experiment_id} acceptance mode differs from the allowlist."
            )
        expected_input_classes = ["SYNTHETIC"]
        if spec.uses_leap_seconds or spec.uses_iers_table:
            expected_input_classes.append("EXTERNAL_AUTHORITATIVE_ARTIFACT")
        if record["inputClasses"] != expected_input_classes:
            raise ProtocolValidationError(
                f"{spec.experiment_id} registry input classes differ from its execution path."
            )


def _scan_fixture_inputs(fixture: Mapping[str, Any]) -> None:
    prohibited = re.compile(
        r"(?:I/311|hip2\.dat|hip7p\.dat|hip9p\.dat|hipvim\.dat|\bHIP\s*\d|catalogue(?:Source)?Bytes)",
        flags=re.IGNORECASE,
    )

    def walk(value: Any, path: str) -> None:
        if isinstance(value, str) and prohibited.search(value):
            raise ProtocolValidationError(
                f"Prohibited catalogue/source material in synthetic input {path}."
            )
        if isinstance(value, Mapping):
            for key, child in value.items():
                if prohibited.search(str(key)):
                    raise ProtocolValidationError(
                        f"Prohibited catalogue/source identifier in synthetic input {path}.{key}."
                    )
                walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")

    walk(fixture["inputs"], "inputs")


def validate_fixture(
    spec: BatchSpec,
    fixture: Mapping[str, Any],
    fixture_bytes: bytes,
    fixture_schema: Mapping[str, Any],
    registry: Mapping[str, Any],
) -> None:
    validate_instance(fixture, fixture_schema)
    if sha256_bytes(fixture_bytes) != EXPECTED_FIXTURE_SHA256[spec.experiment_id]:
        raise ProtocolValidationError(
            f"{spec.experiment_id} fixture bytes differ from the compiled Batch 01 allowlist."
        )
    if fixture["experimentId"] != spec.experiment_id:
        raise ProtocolValidationError("Fixture experiment ID is outside its fixed slot.")
    if fixture["caseId"] != spec.case_id or fixture["fixtureId"] != spec.fixture_id:
        raise ProtocolValidationError("Fixture/case ID does not match the allowlist.")
    if fixture["fixtureId"] != f"{fixture['experimentId']}:{fixture['caseId']}":
        raise ProtocolValidationError("Fixture ID must be experiment ID plus case ID.")
    if tuple(fixture["parameterPartition"]) != spec.partitions:
        raise ProtocolValidationError(
            f"{spec.experiment_id} fixture partitions exceed or differ from Batch 01."
        )
    if fixture["sourceProhibitions"] != SOURCE_PROHIBITIONS:
        raise ProtocolValidationError("Synthetic fixture source prohibitions changed.")
    registry_record = next(
        record
        for record in registry["experiments"]
        if record["experimentId"] == spec.experiment_id
    )
    if fixture["scientificQuestion"] != registry_record["scientificQuestion"]:
        raise ProtocolValidationError("Fixture scientific question differs from registry.")
    assert_ordered_unique(fixture["expectedChecks"], "checkId")
    expected_checks = {
        record["checkId"]: (record["kind"], record["basisClassification"])
        for record in fixture["expectedChecks"]
    }
    compiled_checks = {
        record.check_id: (record.kind, record.basis_classification)
        for record in spec.checks
    }
    if expected_checks != compiled_checks:
        raise ProtocolValidationError("Fixture expected checks differ from allowlist.")
    if fixture["dependencyManifestSha256"] != sha256_file(ENVIRONMENT_PATH):
        raise ProtocolValidationError("Fixture dependency-manifest hash is stale.")
    if fixture["registrySha256"] != sha256_file(REGISTRY_PATH):
        raise ProtocolValidationError("Fixture registry hash is stale.")
    if fixture["fixtureSchemaSha256"] != sha256_file(FIXTURE_SCHEMA_PATH):
        raise ProtocolValidationError("Fixture-schema hash is stale.")
    if fixture_bytes != canonical_experiment_bytes(fixture):
        raise ProtocolValidationError("Fixture is not canonical experiment JSON.")
    _scan_fixture_inputs(fixture)
    used_records = [
        (record["role"], record["artifactId"])
        for record in fixture["usedArtifactHashes"]
    ]
    if used_records != sorted(used_records) or len(used_records) != len(
        set(used_records)
    ):
        raise ProtocolValidationError(
            "Used fixture artifacts must have stable unique role/ID order."
        )
    used_ids = [record["artifactId"] for record in fixture["usedArtifactHashes"]]
    environment = read_json_strict(ENVIRONMENT_PATH)
    package_version = next(
        record["version"]
        for record in environment["resolvedRuntimePackages"]
        if record["name"] == "astropy-iers-data"
    )
    environment_artifacts = {
        f"astropy-iers-data/{Path(record['packageResource']).name}": {
            "artifactId": f"astropy-iers-data/{Path(record['packageResource']).name}",
            "classification": "EXTERNAL_AUTHORITATIVE_ARTIFACT",
            "role": record["role"],
            "sha256": record["sha256"],
            "version": package_version,
        }
        for record in environment["iersPolicy"]["files"]
    }
    expected_artifact_ids = set()
    if spec.uses_leap_seconds:
        expected_artifact_ids.add("astropy-iers-data/Leap_Second.dat")
    if spec.uses_iers_table:
        expected_artifact_ids.add("astropy-iers-data/finals2000A.all")
    if set(used_ids) != expected_artifact_ids:
        raise ProtocolValidationError(
            f"{spec.experiment_id} external-artifact inventory differs from its fixed execution path."
        )
    for record in fixture["usedArtifactHashes"]:
        if record != environment_artifacts.get(record["artifactId"]):
            raise ProtocolValidationError(
                f"{spec.experiment_id} external-artifact provenance differs from the environment manifest."
            )
    actual_artifact_paths = {
        "astropy-iers-data/Leap_Second.dat": Path(
            astropy_iers_data.IERS_LEAP_SECOND_FILE
        ),
        "astropy-iers-data/finals2000A.all": Path(astropy_iers_data.IERS_A_FILE),
    }
    for artifact_id in expected_artifact_ids:
        if sha256_file(actual_artifact_paths[artifact_id]) != environment_artifacts[
            artifact_id
        ]["sha256"]:
            raise ProtocolValidationError(
                f"{artifact_id} bytes differ from pinned environment evidence."
            )


def _isolated_evidence(
    spec: BatchSpec, fixture: Mapping[str, Any]
) -> dict[str, Any]:
    handler = HANDLERS.get(spec.handler)
    if handler is None:
        raise ProtocolValidationError(f"Missing Batch 01 handler {spec.handler}.")
    with tempfile.TemporaryDirectory(prefix="ufuq-batch01-cache-") as cache:
        with ExitStack() as stack:
            stack.enter_context(set_temp_cache(cache))
            stack.enter_context(iers.conf.set_temp("auto_download", False))
            stack.enter_context(iers.conf.set_temp("iers_degraded_accuracy", "error"))
            stack.enter_context(data_conf.set_temp("allow_internet", False))
            stack.enter_context(network_blocked())
            outer_caught = stack.enter_context(warnings.catch_warnings(record=True))
            warnings.simplefilter("always")
            if spec.uses_leap_seconds:
                leap = iers.LeapSeconds.open(astropy_iers_data.IERS_LEAP_SECOND_FILE)
                leap.update_erfa_leap_seconds(initialize_erfa="empty")
            if spec.uses_iers_table:
                table = iers.IERS_A.open(astropy_iers_data.IERS_A_FILE)
                stack.enter_context(iers.earth_orientation_table.set(table))
            evidence = handler(spec, fixture)
            evidence["warnings"] = _merge_warning_records(
                evidence["warnings"], _warning_records(outer_caught)
            )
            return evidence


def _external_artifact_provenance(fixture: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "artifactId": record["artifactId"],
            "role": record["role"],
            "sha256": record["sha256"],
            "version": record["version"],
        }
        for record in fixture["usedArtifactHashes"]
        if record["classification"] == "EXTERNAL_AUTHORITATIVE_ARTIFACT"
    ]


def _runner_source_files() -> list[dict[str, str]]:
    paths = [
        PROJECT_ROOT / "run.py",
        PROJECT_ROOT / "src" / "ufuq_astronomy_reference" / "__init__.py",
        PROJECT_ROOT / "src" / "ufuq_astronomy_reference" / "batch01.py",
        PROJECT_ROOT
        / "src"
        / "ufuq_astronomy_reference"
        / "experiment_protocol.py",
        PROJECT_ROOT / "src" / "ufuq_astronomy_reference" / "oracle.py",
    ]
    return [
        {
            "path": path.relative_to(PROJECT_ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for path in sorted(paths, key=lambda item: item.as_posix())
    ]


def _manifest(
    spec: BatchSpec,
    fixture: Mapping[str, Any],
    fixture_bytes: bytes,
    environment: Mapping[str, Any],
) -> dict[str, Any]:
    versions = {
        record["name"]: record["version"]
        for record in environment["resolvedRuntimePackages"]
    }
    dependency_kinds = {
        record["name"]: record["dependencyKind"]
        for record in environment["resolvedRuntimePackages"]
    }
    return {
        "cachePolicy": "FRESH_ISOLATED_CACHE_NO_DISCOVERY",
        "canonicalSerialization": "UFUQ_CANONICAL_JSON_V1",
        "caseId": spec.case_id,
        "comparisonLineage": spec.comparison_lineage,
        "experimentId": spec.experiment_id,
        "externalArtifactProvenance": _external_artifact_provenance(fixture),
        "fixtureId": spec.fixture_id,
        "fixtureSchemaVersion": "ufuq.astronomy-experiment-fixture.v1",
        "hashes": {
            "environmentManifestSha256": sha256_file(ENVIRONMENT_PATH),
            "fixtureByteLength": len(fixture_bytes),
            "fixtureSchemaSha256": sha256_file(FIXTURE_SCHEMA_PATH),
            "fixtureSha256": sha256_bytes(fixture_bytes),
            "lockfileSha256": sha256_file(LOCK_PATH),
            "protocolDocumentSha256": sha256_file(PROTOCOL_PATH),
            "registrySchemaSha256": sha256_file(REGISTRY_SCHEMA_PATH),
            "registrySha256": sha256_file(REGISTRY_PATH),
            "resultSchemaSha256": sha256_file(RESULT_SCHEMA_PATH),
        },
        "manifestVersion": "ufuq.astronomy-experiment-execution-manifest.v1",
        "networkPolicy": "OFFLINE_AUTO_DOWNLOAD_DISABLED",
        "protocolVersion": "2C.5A-v1",
        "recordOrdering": "REGISTRY_ID_GROUP_MEMBER_INPUT_KEY_MEASUREMENT_ID_STATUS_SEQUENCE_CHECK_ID",
        "registryVersion": "ufuq.astronomy-experiment-registry.v1",
        "repetitionCount": 2,
        "resultSchemaVersion": "ufuq.astronomy-experiment-result.v1",
        "runner": {
            "argv": ["run.py", "batch-01"],
            "entryPoint": "run.py",
            "runnerId": RUNNER_ID,
            "runnerVersion": RUNNER_VERSION,
            "sourceFiles": _runner_source_files(),
            "workingDirectory": "tools/astronomy-reference",
        },
        "runtimeContext": {
            "architecture": platform.machine(),
            "operatingSystem": platform.system(),
            "operatingSystemVersion": platform.version(),
            "pythonImplementation": platform.python_implementation(),
        },
        "softwareRuntime": {
            "astropyIersDataVersion": versions["astropy-iers-data"],
            "astropyVersion": versions["astropy"],
            "directlyImportedPackages": ["astropy", "astropy_iers_data", "erfa"],
            "erfaVersion": erfa.version.erfa_version,
            "pyerfaDependencyKind": dependency_kinds["pyerfa"],
            "pyerfaVersion": importlib.metadata.version("pyerfa"),
            "pythonVersion": platform.python_version(),
            "sofaIssue": erfa.version.sofa_version,
            "uvVersion": "0.11.32",
        },
    }


def _build_result(
    spec: BatchSpec,
    fixture: Mapping[str, Any],
    fixture_bytes: bytes,
    environment: Mapping[str, Any],
) -> dict[str, Any]:
    first = _isolated_evidence(spec, fixture)
    second = _isolated_evidence(spec, fixture)
    if canonical_experiment_bytes(first) != canonical_experiment_bytes(second):
        raise ProtocolValidationError(
            f"{spec.experiment_id} internal isolated repetitions differ."
        )
    result: dict[str, Any] = {
        "caseId": spec.case_id,
        "checks": first["checks"],
        "decisionLimits": DECISION_LIMITS,
        "errorBudgetStatus": "NOT_ESTABLISHED_AST_006_OPEN",
        "executionManifest": _manifest(spec, fixture, fixture_bytes, environment),
        "executionOutcome": {"reasons": [], "state": "COMPLETED"},
        "experimentId": spec.experiment_id,
        "fixtureId": spec.fixture_id,
        "measurements": first["measurements"],
        "resultClassification": RESULT_CLASSIFICATION,
        "schemaVersion": "ufuq.astronomy-experiment-result.v1",
        "structuredStatuses": first["structuredStatuses"],
        "warnings": first["warnings"],
    }
    result["canonicalContentSha256"] = sha256_bytes(
        canonical_experiment_bytes(result)
    )
    return result


def _load_fixture(
    spec: BatchSpec,
    fixture_schema: Mapping[str, Any],
    registry: Mapping[str, Any],
) -> tuple[dict[str, Any], bytes]:
    path = FIXTURE_ROOT / spec.fixture_filename
    fixture = read_json_strict(path, require_canonical=True)
    fixture_bytes = path.read_bytes()
    validate_fixture(spec, fixture, fixture_bytes, fixture_schema, registry)
    return fixture, fixture_bytes


def run_batch01(
    *,
    experiment_ids: list[str] | None = None,
    write_results: bool = True,
) -> dict[str, bytes]:
    """Run only the fixed Batch 01 allowlist and return canonical result bytes."""

    requested = list(SPEC_BY_ID) if experiment_ids is None else experiment_ids
    if not requested:
        raise ProtocolValidationError("Batch 01 requires at least one allowlisted ID.")
    if len(requested) != len(set(requested)):
        raise ProtocolValidationError("Duplicate requested experiment ID.")
    unknown = set(requested) - set(SPEC_BY_ID)
    if unknown:
        raise ProtocolValidationError(
            f"Unknown or non-Batch experiment IDs rejected: {sorted(unknown)}."
        )
    if write_results and set(requested) != set(SPEC_BY_ID):
        raise ProtocolValidationError(
            "Canonical Batch 01 evidence writes require the complete nine-experiment allowlist."
        )
    schemas = _schema_bundle()
    registry = read_json_strict(REGISTRY_PATH)
    validate_registry(registry, schemas["registry"])
    environment = read_json_strict(ENVIRONMENT_PATH)
    if environment != build_environment_manifest(PROJECT_ROOT):
        raise ProtocolValidationError(
            "Installed runtime or packaged artifact evidence differs from the environment manifest."
        )
    if environment["lock"]["sha256"] != sha256_file(LOCK_PATH):
        raise ProtocolValidationError("Environment manifest lock hash is stale.")
    runtime_kinds = {
        item["name"]: item["dependencyKind"]
        for item in environment["resolvedRuntimePackages"]
    }
    if runtime_kinds.get("pyerfa") != "DIRECT":
        raise ProtocolValidationError("PyERFA must be a direct Batch 01 dependency.")

    outputs: dict[str, bytes] = {}
    for spec in BATCH_SPECS:
        if spec.experiment_id not in requested:
            continue
        fixture, fixture_bytes = _load_fixture(
            spec, schemas["fixture"], registry
        )
        result = _build_result(spec, fixture, fixture_bytes, environment)
        validate_instance(result, schemas["result"])
        output = canonical_experiment_bytes(result)
        outputs[spec.result_filename] = output
    if write_results:
        RESULT_ROOT.mkdir(parents=True, exist_ok=True)
        for filename, output in sorted(outputs.items()):
            result_path = RESULT_ROOT / filename
            hash_path = result_path.with_suffix(".sha256")
            result_path.write_bytes(output)
            hash_path.write_text(sha256_bytes(output) + "\n", encoding="ascii", newline="\n")
    return outputs


def validate_batch01_artifacts() -> None:
    """Validate every committed Batch 01 fixture/result and hash boundary."""

    schemas = _schema_bundle()
    registry = read_json_strict(REGISTRY_PATH)
    validate_registry(registry, schemas["registry"])
    expected_fixtures = {spec.fixture_filename for spec in BATCH_SPECS}
    actual_fixtures = {path.name for path in FIXTURE_ROOT.iterdir()}
    if actual_fixtures != expected_fixtures:
        raise ProtocolValidationError("Batch 01 fixture inventory differs from allowlist.")
    expected_results = {spec.result_filename for spec in BATCH_SPECS}
    expected_companions = {
        Path(filename).with_suffix(".sha256").name
        for filename in expected_results
    }
    actual_result_files = {path.name for path in RESULT_ROOT.iterdir()}
    if actual_result_files != expected_results | expected_companions:
        raise ProtocolValidationError("Batch 01 result inventory differs from allowlist.")

    environment = read_json_strict(ENVIRONMENT_PATH)
    if environment != build_environment_manifest(PROJECT_ROOT):
        raise ProtocolValidationError(
            "Installed runtime or packaged artifact evidence differs from the environment manifest."
        )
    for spec in BATCH_SPECS:
        fixture, fixture_bytes = _load_fixture(spec, schemas["fixture"], registry)
        result_path = RESULT_ROOT / spec.result_filename
        result = read_json_strict(result_path, require_canonical=True)
        validate_instance(result, schemas["result"])
        if result["experimentId"] != spec.experiment_id:
            raise ProtocolValidationError("Result experiment ID differs from allowlist.")
        if result["fixtureId"] != fixture["fixtureId"] or result["caseId"] != fixture["caseId"]:
            raise ProtocolValidationError("Result identity differs from fixture identity.")
        manifest = result["executionManifest"]
        if manifest["experimentId"] != result["experimentId"]:
            raise ProtocolValidationError("Manifest experiment ID differs from result.")
        if manifest["fixtureId"] != result["fixtureId"] or manifest["caseId"] != result["caseId"]:
            raise ProtocolValidationError("Manifest fixture identity differs from result.")
        if manifest["comparisonLineage"] != spec.comparison_lineage:
            raise ProtocolValidationError("Result lineage differs from registry allowlist.")
        expected_manifest = _manifest(spec, fixture, fixture_bytes, environment)
        if manifest != expected_manifest:
            raise ProtocolValidationError("Result execution manifest is stale.")
        content_body = dict(result)
        recorded_content_hash = content_body.pop("canonicalContentSha256")
        if recorded_content_hash != sha256_bytes(canonical_experiment_bytes(content_body)):
            raise ProtocolValidationError("Result canonical-content hash is invalid.")
        result_bytes = result_path.read_bytes()
        companion = result_path.with_suffix(".sha256").read_bytes()
        expected_companion = (sha256_bytes(result_bytes) + "\n").encode("ascii")
        if companion != expected_companion:
            raise ProtocolValidationError("Result full-file companion hash is invalid.")
        expected_check_contract = [
            (check.check_id, check.kind, check.basis_classification)
            for check in sorted(spec.checks, key=lambda item: item.check_id)
        ]
        actual_check_contract = [
            (
                check["checkId"],
                check["kind"],
                check["basisClassification"],
            )
            for check in result["checks"]
        ]
        if actual_check_contract != expected_check_contract:
            raise ProtocolValidationError("Result check contract differs from allowlist.")
        if any(
            check["kind"] == "MEASUREMENT_ONLY"
            and check["status"] != "MEASURED_NO_ACCEPTANCE"
            for check in result["checks"]
        ):
            raise ProtocolValidationError("A measurement-only check gained acceptance.")
        if any(
            measurement["acceptanceStatus"] != "MEASURED_NO_ACCEPTANCE"
            for measurement in result["measurements"]
        ):
            raise ProtocolValidationError("A numerical measurement gained acceptance.")
