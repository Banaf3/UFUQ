"""Independent, synthetic-only UFUQ astronomy reference fixture producer."""

from .oracle import (
    InputValidationError,
    UnexpectedNetworkAccess,
    build_environment_manifest,
    canonical_bytes,
    generate_fixture,
    sha256_bytes,
)
from .batch01 import (
    BATCH_SPECS,
    ProtocolValidationError,
    run_batch01,
    validate_batch01_artifacts,
)

__all__ = [
    "InputValidationError",
    "UnexpectedNetworkAccess",
    "BATCH_SPECS",
    "ProtocolValidationError",
    "build_environment_manifest",
    "canonical_bytes",
    "generate_fixture",
    "run_batch01",
    "sha256_bytes",
    "validate_batch01_artifacts",
]

__version__ = "0.1.0"
