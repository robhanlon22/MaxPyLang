"""Tests for typecheck helpers."""

from maxpylang.tools import typechecks


def test_typecheck_helpers_cover_numeric_and_dispatch_paths() -> None:
    """Verify numeric and type helper dispatch behavior."""
    assert typechecks.check_number("3.14") is True
    assert typechecks.check_number("nope") is False
    assert typechecks.check_any(object()) is True
    assert typechecks.check_int("7") is True
    assert typechecks.check_int("7.5") is False
    assert typechecks.check_type(["float"], "8.25") is True
    assert typechecks.check_type(["symbol", "int"], "hello") is True
    assert typechecks.check_type(["int"], "hello") is False
