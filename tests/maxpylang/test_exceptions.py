"""Tests for package exceptions."""

from maxpylang.exceptions import UnknownObjectWarning


def test_unknown_object_warning_is_user_warning() -> None:
    """Ensure warning subclasses are inherited as expected."""
    assert issubclass(UnknownObjectWarning, UserWarning)
    assert issubclass(UnknownObjectWarning, Warning)
