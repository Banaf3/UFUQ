"""Independent, synthetic-only UFUQ astronomy reference fixture producer."""

from .oracle import (
    InputValidationError,
    UnexpectedNetworkAccess,
    build_environment_manifest,
    canonical_bytes,
    generate_fixture,
    sha256_bytes,
)

__all__ = [
    "InputValidationError",
    "UnexpectedNetworkAccess",
    "build_environment_manifest",
    "canonical_bytes",
    "generate_fixture",
    "sha256_bytes",
]

__version__ = "0.1.0"
