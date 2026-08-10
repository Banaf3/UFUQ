"""Fail-closed protocol utilities for synthetic Milestone 2C.5B evidence.

The validator intentionally implements only the Draft 2020-12 keywords used by the
three committed experiment schemas. Unknown keywords and non-local references fail.
It is not a general UFUQ runtime-validator selection.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import unicodedata
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


CANONICAL_SERIALIZATION = "UFUQ_CANONICAL_JSON_V1"
JSON_SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"
MAX_EXACT_BINARY64_INTEGER = 2**53
SUPPORTED_SCHEMA_KEYWORDS = {
    "$defs",
    "$id",
    "$ref",
    "$schema",
    "additionalProperties",
    "allOf",
    "const",
    "contains",
    "description",
    "else",
    "enum",
    "if",
    "items",
    "maxItems",
    "minItems",
    "minLength",
    "minProperties",
    "minimum",
    "not",
    "oneOf",
    "pattern",
    "properties",
    "propertyNames",
    "prefixItems",
    "required",
    "then",
    "title",
    "type",
    "uniqueItems",
}
SUPPORTED_SCHEMA_TYPES = {
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
}


class ProtocolValidationError(ValueError):
    """Raised when canonical bytes, a schema, or an instance fail closed."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_string(value: str) -> str:
    return json.dumps(
        unicodedata.normalize("NFC", value),
        ensure_ascii=False,
        separators=(",", ":"),
    )


def _json_number(value: int | float) -> str:
    if isinstance(value, bool):
        raise ProtocolValidationError("Booleans are not canonical JSON numbers.")
    if isinstance(value, int):
        return str(value)
    if not math.isfinite(value):
        raise ProtocolValidationError("Canonical JSON forbids non-finite numbers.")
    if value == 0.0:
        if math.copysign(1.0, value) < 0:
            raise ProtocolValidationError("Canonical JSON forbids negative zero.")
        return "0"
    rendered = repr(value).lower()
    if "e" in rendered:
        mantissa, exponent = rendered.split("e", 1)
        if mantissa.endswith(".0"):
            mantissa = mantissa[:-2]
        rendered = f"{mantissa}e{int(exponent)}"
    elif rendered.endswith(".0"):
        rendered = rendered[:-2]
    return rendered


def _render_canonical(
    value: Any, level: int, *, containing_key: str | None = None
) -> str:
    indent = "  " * level
    child_indent = "  " * (level + 1)
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int) and not isinstance(value, bool):
        if containing_key == "fixtureByteLength":
            if value < 0:
                raise ProtocolValidationError(
                    "Canonical byte counts must be non-negative integers."
                )
        elif abs(value) > MAX_EXACT_BINARY64_INTEGER:
            raise ProtocolValidationError(
                "Canonical JSON integers must fit the exact binary64 integer range."
            )
        return _json_number(value)
    if isinstance(value, float):
        return _json_number(value)
    if isinstance(value, str):
        return _json_string(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        rendered = [
            f"{child_indent}{_render_canonical(item, level + 1)}"
            for item in value
        ]
        return "[\n" + ",\n".join(rendered) + f"\n{indent}]"
    if isinstance(value, Mapping):
        if not value:
            return "{}"
        if not all(isinstance(key, str) for key in value):
            raise ProtocolValidationError("Canonical JSON object keys must be strings.")
        normalized_items: dict[str, Any] = {}
        for key, item in value.items():
            normalized_key = unicodedata.normalize("NFC", key)
            if normalized_key in normalized_items:
                raise ProtocolValidationError(
                    "Canonical JSON object keys collide after NFC normalization."
                )
            normalized_items[normalized_key] = item
        rendered = [
            (
                f"{child_indent}{_json_string(key)}: "
                f"{_render_canonical(normalized_items[key], level + 1, containing_key=key)}"
            )
            for key in sorted(normalized_items)
        ]
        return "{\n" + ",\n".join(rendered) + f"\n{indent}}}"
    raise ProtocolValidationError(
        f"Unsupported canonical JSON value type: {type(value).__name__}."
    )


def canonical_experiment_bytes(value: Any) -> bytes:
    """Return canonical experiment JSON bytes with exactly one terminal LF."""

    return (_render_canonical(value, 0) + "\n").encode("utf-8")


def _pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ProtocolValidationError(f"Duplicate JSON object key: {key!r}.")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ProtocolValidationError(f"Non-JSON numeric constant: {value}.")


def read_json_strict(path: Path, *, require_canonical: bool = False) -> dict[str, Any]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ProtocolValidationError(f"{path.name} contains a UTF-8 BOM.")
    if b"\r" in raw:
        raise ProtocolValidationError(f"{path.name} must use LF line endings.")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ProtocolValidationError(f"{path.name} is not UTF-8.") from error
    try:
        value = json.loads(
            text,
            object_pairs_hook=_pairs_no_duplicates,
            parse_constant=_reject_constant,
        )
    except json.JSONDecodeError as error:
        raise ProtocolValidationError(f"Invalid JSON in {path.name}: {error}.") from error
    if not isinstance(value, dict):
        raise ProtocolValidationError(f"{path.name} must contain a JSON object.")
    if require_canonical and raw != canonical_experiment_bytes(value):
        raise ProtocolValidationError(
            f"{path.name} is not {CANONICAL_SERIALIZATION} canonical JSON."
        )
    return value


def _schema_children(schema: Mapping[str, Any]) -> list[tuple[str, Mapping[str, Any]]]:
    children: list[tuple[str, Mapping[str, Any]]] = []
    for collection_name in ("$defs", "properties"):
        collection = schema.get(collection_name, {})
        if collection:
            if not isinstance(collection, Mapping):
                raise ProtocolValidationError(
                    f"Schema keyword {collection_name} must be an object."
                )
            for name, child in collection.items():
                if not isinstance(child, Mapping):
                    raise ProtocolValidationError(
                        f"Schema {collection_name}/{name} must be an object."
                    )
                children.append((f"{collection_name}/{name}", child))
    for collection_name in ("allOf", "oneOf", "prefixItems"):
        collection = schema.get(collection_name, [])
        if collection:
            if not isinstance(collection, list):
                raise ProtocolValidationError(
                    f"Schema keyword {collection_name} must be an array."
                )
            for index, child in enumerate(collection):
                if not isinstance(child, Mapping):
                    raise ProtocolValidationError(
                        f"Schema {collection_name}/{index} must be an object."
                    )
                children.append((f"{collection_name}/{index}", child))
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
        child = schema.get(name)
        if isinstance(child, Mapping):
            children.append((name, child))
    return children


def _validate_schema_keyword_shapes(node: Mapping[str, Any], path: str) -> None:
    """Reject unsupported keyword value shapes instead of silently ignoring them."""

    if path != "#":
        scoped_keywords = {"$defs", "$id", "$schema"}.intersection(node)
        if scoped_keywords:
            raise ProtocolValidationError(
                "Nested schema scope keywords are outside the local Batch 01 "
                f"subset at {path}: {sorted(scoped_keywords)}."
            )
    for name in ("$id", "$ref", "$schema", "description", "pattern", "title"):
        if name in node and not isinstance(node[name], str):
            raise ProtocolValidationError(
                f"Schema keyword {name} must be a string at {path}."
            )
    if "$schema" in node and node["$schema"] != JSON_SCHEMA_DIALECT:
        raise ProtocolValidationError(
            f"Schema keyword $schema must declare Draft 2020-12 at {path}."
        )
    if "pattern" in node:
        try:
            re.compile(node["pattern"])
        except re.error as error:
            raise ProtocolValidationError(
                f"Schema keyword pattern is invalid at {path}: {error}."
            ) from error

    expected_type = node.get("type")
    if expected_type is not None and (
        not isinstance(expected_type, str)
        or expected_type not in SUPPORTED_SCHEMA_TYPES
    ):
        raise ProtocolValidationError(
            f"Schema keyword type is unsupported at {path}: {expected_type!r}."
        )

    for name in ("$defs", "properties"):
        if name not in node:
            continue
        collection = node[name]
        if not isinstance(collection, Mapping):
            raise ProtocolValidationError(
                f"Schema keyword {name} must be an object at {path}."
            )
        if not all(
            isinstance(key, str) and isinstance(child, Mapping)
            for key, child in collection.items()
        ):
            raise ProtocolValidationError(
                f"Schema keyword {name} must map strings to schema objects at {path}."
            )

    for name in ("allOf", "oneOf", "prefixItems"):
        if name not in node:
            continue
        collection = node[name]
        if not isinstance(collection, list) or not collection or not all(
            isinstance(child, Mapping) for child in collection
        ):
            raise ProtocolValidationError(
                f"Schema keyword {name} must be a non-empty array of schema "
                f"objects at {path}."
            )

    for name in ("contains", "else", "if", "not", "propertyNames", "then"):
        if name in node and not isinstance(node[name], Mapping):
            raise ProtocolValidationError(
                f"Schema keyword {name} must be a schema object at {path}."
            )
    for name in ("additionalProperties", "items"):
        if name in node and not isinstance(node[name], (bool, Mapping)):
            raise ProtocolValidationError(
                f"Schema keyword {name} must be a Boolean or schema object at {path}."
            )

    if "required" in node:
        required = node["required"]
        if (
            not isinstance(required, list)
            or not all(isinstance(name, str) for name in required)
            or len(required) != len(set(required))
        ):
            raise ProtocolValidationError(
                f"Schema keyword required must be an array of unique strings at {path}."
            )
    if "enum" in node:
        candidates = node["enum"]
        if not isinstance(candidates, list) or not candidates:
            raise ProtocolValidationError(
                f"Schema keyword enum must be a non-empty array at {path}."
            )
        identities = [
            canonical_experiment_bytes({"value": candidate})
            for candidate in candidates
        ]
        if len(identities) != len(set(identities)):
            raise ProtocolValidationError(
                f"Schema keyword enum must contain unique values at {path}."
            )
    if "const" in node:
        canonical_experiment_bytes({"value": node["const"]})

    for name in ("maxItems", "minItems", "minLength", "minProperties"):
        if name not in node:
            continue
        value = node[name]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ProtocolValidationError(
                f"Schema keyword {name} must be a non-negative integer at {path}."
            )
    if "minimum" in node:
        value = node["minimum"]
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
        ):
            raise ProtocolValidationError(
                f"Schema keyword minimum must be a finite number at {path}."
            )
    if "uniqueItems" in node and not isinstance(node["uniqueItems"], bool):
        raise ProtocolValidationError(
            f"Schema keyword uniqueItems must be a Boolean at {path}."
        )


def validate_schema_contract(schema: Mapping[str, Any]) -> None:
    """Validate the closed local schema subset used by Batch 01.

    This checks local references and refuses unsupported keywords. It deliberately
    does not claim full official meta-schema conformance.
    """

    if schema.get("$schema") != JSON_SCHEMA_DIALECT:
        raise ProtocolValidationError("Schema must declare Draft 2020-12.")
    definitions = schema.get("$defs", {})
    if not isinstance(definitions, Mapping):
        raise ProtocolValidationError("Schema keyword $defs must be an object at #.")

    def walk(node: Mapping[str, Any], path: str) -> None:
        unknown = set(node) - SUPPORTED_SCHEMA_KEYWORDS
        if unknown:
            raise ProtocolValidationError(
                f"Unsupported schema keywords at {path}: {sorted(unknown)}."
            )
        _validate_schema_keyword_shapes(node, path)
        reference = node.get("$ref")
        if reference is not None:
            if not isinstance(reference, str) or not reference.startswith("#/$defs/"):
                raise ProtocolValidationError(
                    f"Only local $defs references are permitted at {path}."
                )
            if reference.removeprefix("#/$defs/") not in definitions:
                raise ProtocolValidationError(
                    f"Unresolved local schema reference at {path}: {reference}."
                )
        for name, child in _schema_children(node):
            walk(child, f"{path}/{name}")

    walk(schema, "#")


def _json_equal(left: Any, right: Any) -> bool:
    return canonical_experiment_bytes({"value": left}) == canonical_experiment_bytes(
        {"value": right}
    )


def _matches_type(instance: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(instance, Mapping)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "null":
        return instance is None
    if expected == "number":
        return (
            not isinstance(instance, bool)
            and isinstance(instance, (int, float))
            and (not isinstance(instance, float) or math.isfinite(instance))
        )
    if expected == "integer":
        return (
            not isinstance(instance, bool)
            and isinstance(instance, (int, float))
            and (not isinstance(instance, float) or (math.isfinite(instance) and instance.is_integer()))
        )
    raise ProtocolValidationError(f"Unsupported schema type: {expected}.")


def validate_instance(
    instance: Any,
    schema: Mapping[str, Any] | bool,
    *,
    root_schema: Mapping[str, Any] | None = None,
    path: str = "$",
) -> None:
    """Validate an instance against the closed schema keyword subset."""

    if schema is True:
        return
    if schema is False:
        raise ProtocolValidationError(f"{path} is rejected by a false schema.")
    root = schema if root_schema is None else root_schema
    reference = schema.get("$ref")
    if reference is not None:
        name = str(reference).removeprefix("#/$defs/")
        validate_instance(instance, root["$defs"][name], root_schema=root, path=path)

    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not _matches_type(instance, expected_type):
        raise ProtocolValidationError(
            f"{path} must have JSON Schema type {expected_type}."
        )
    if "const" in schema and not _json_equal(instance, schema["const"]):
        raise ProtocolValidationError(f"{path} does not match its const value.")
    if "enum" in schema and not any(
        _json_equal(instance, candidate) for candidate in schema["enum"]
    ):
        raise ProtocolValidationError(f"{path} is not in its schema enum.")
    if "not" in schema:
        try:
            validate_instance(instance, schema["not"], root_schema=root, path=path)
        except ProtocolValidationError:
            pass
        else:
            raise ProtocolValidationError(f"{path} matches a prohibited schema.")
    if "oneOf" in schema:
        matches = 0
        for candidate in schema["oneOf"]:
            try:
                validate_instance(instance, candidate, root_schema=root, path=path)
            except ProtocolValidationError:
                continue
            matches += 1
        if matches != 1:
            raise ProtocolValidationError(
                f"{path} must match exactly one oneOf branch; matched {matches}."
            )
    for candidate in schema.get("allOf", []):
        validate_instance(instance, candidate, root_schema=root, path=path)

    condition = schema.get("if")
    if isinstance(condition, Mapping):
        try:
            validate_instance(instance, condition, root_schema=root, path=path)
        except ProtocolValidationError:
            branch = schema.get("else")
        else:
            branch = schema.get("then")
        if isinstance(branch, Mapping):
            validate_instance(instance, branch, root_schema=root, path=path)

    if isinstance(instance, Mapping):
        required = schema.get("required", [])
        missing = [name for name in required if name not in instance]
        if missing:
            raise ProtocolValidationError(f"{path} is missing required keys {missing}.")
        minimum_properties = schema.get("minProperties")
        if isinstance(minimum_properties, int) and len(instance) < minimum_properties:
            raise ProtocolValidationError(
                f"{path} has fewer than {minimum_properties} properties."
            )
        property_names = schema.get("propertyNames")
        if isinstance(property_names, Mapping):
            for name in instance:
                validate_instance(
                    name,
                    property_names,
                    root_schema=root,
                    path=f"{path}.<propertyName>",
                )
        properties = schema.get("properties", {})
        for name, child_schema in properties.items():
            if name in instance:
                validate_instance(
                    instance[name],
                    child_schema,
                    root_schema=root,
                    path=f"{path}.{name}",
                )
        extras = set(instance) - set(properties)
        additional = schema.get("additionalProperties", True)
        if additional is False and extras:
            raise ProtocolValidationError(
                f"{path} has unknown properties {sorted(extras)}."
            )
        if isinstance(additional, Mapping):
            for name in extras:
                validate_instance(
                    instance[name],
                    additional,
                    root_schema=root,
                    path=f"{path}.{name}",
                )

    if isinstance(instance, list):
        minimum = schema.get("minItems")
        maximum = schema.get("maxItems")
        if isinstance(minimum, int) and len(instance) < minimum:
            raise ProtocolValidationError(f"{path} has fewer than {minimum} items.")
        if isinstance(maximum, int) and len(instance) > maximum:
            raise ProtocolValidationError(f"{path} has more than {maximum} items.")
        if schema.get("uniqueItems"):
            identities = [canonical_experiment_bytes({"value": item}) for item in instance]
            if len(identities) != len(set(identities)):
                raise ProtocolValidationError(f"{path} must contain unique items.")
        prefix_items = schema.get("prefixItems", [])
        for index, prefix_schema in enumerate(prefix_items):
            if index < len(instance):
                validate_instance(
                    instance[index],
                    prefix_schema,
                    root_schema=root,
                    path=f"{path}[{index}]",
                )
        item_schema = schema.get("items")
        start_index = len(prefix_items)
        if item_schema is False and len(instance) > start_index:
            raise ProtocolValidationError(
                f"{path} contains items beyond its prefixItems schema."
            )
        if isinstance(item_schema, Mapping):
            for index, item in enumerate(instance[start_index:], start=start_index):
                validate_instance(item, item_schema, root_schema=root, path=f"{path}[{index}]")
        contains = schema.get("contains")
        if isinstance(contains, Mapping):
            matched = False
            for item in instance:
                try:
                    validate_instance(item, contains, root_schema=root, path=path)
                except ProtocolValidationError:
                    continue
                matched = True
                break
            if not matched:
                raise ProtocolValidationError(
                    f"{path} does not contain an item matching contains."
                )

    if isinstance(instance, str):
        minimum_length = schema.get("minLength")
        if isinstance(minimum_length, int) and len(instance) < minimum_length:
            raise ProtocolValidationError(
                f"{path} is shorter than {minimum_length} characters."
            )
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, instance) is None:
            raise ProtocolValidationError(f"{path} does not match {pattern!r}.")

    if _matches_type(instance, "number"):
        minimum = schema.get("minimum")
        if isinstance(minimum, (int, float)) and instance < minimum:
            raise ProtocolValidationError(f"{path} is below minimum {minimum}.")


def assert_ordered_unique(records: Sequence[Mapping[str, Any]], key: str) -> None:
    values = [str(record[key]) for record in records]
    if values != sorted(values) or len(values) != len(set(values)):
        raise ProtocolValidationError(
            f"Records must be uniquely ordered by {key}: {values}."
        )
