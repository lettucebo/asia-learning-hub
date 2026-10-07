import hashlib
import re

RULES_FILE = "CONTRIBUTING.md"
SHA_PATTERN = re.compile(r"[0-9a-f]{40}")
_CHECKS_HEADING = re.compile(r"^## Review checks\s*$", re.MULTILINE)
_NEXT_HEADING = re.compile(r"^## ", re.MULTILINE)
_CHECK_ROW = re.compile(r"^\|\s*([A-Z]+-\d{2})\s*\|", re.MULTILINE)


def parse_rule_ids(contributing: str) -> list[str]:
    """Return the check IDs defined in the "Review checks" table, in order."""
    heading = _CHECKS_HEADING.search(contributing)
    if heading is None:
        raise ValueError(f"{RULES_FILE} has no '## Review checks' section")
    section = contributing[heading.end():]
    following = _NEXT_HEADING.search(section)
    if following:
        section = section[:following.start()]
    ids = _CHECK_ROW.findall(section)
    if not ids:
        raise ValueError(f"{RULES_FILE} defines no review check IDs")
    if len(set(ids)) != len(ids):
        raise ValueError(f"{RULES_FILE} defines a review check ID twice")
    return ids


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require_sha(value: str, name: str) -> str:
    if not SHA_PATTERN.fullmatch(value):
        raise ValueError(f"Invalid {name} SHA")
    return value
