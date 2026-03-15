"""Tests for objfuncs.args helpers."""

import pytest

from maxpylang import MaxObject
from maxpylang.exceptions import UnknownObjectWarning


def test_args_valid_reports_missing_and_type_warnings(
    caplog: object,
) -> None:
    """Verify warnings are emitted for missing or mistyped arguments."""
    obj = MaxObject("toggle")
    arg_info = {
        "required": [{"name": "freq", "type": ["number"]}],
        "optional": [{"name": "label", "type": ["symbol"]}],
    }
    strict_optional = {
        "required": [{"name": "freq", "type": ["number"]}],
        "optional": [{"name": "count", "type": ["int"]}],
    }

    assert obj.args_valid("osc", [440], arg_info) is True
    assert "(arg_warning):" in caplog.text

    with pytest.warns(UnknownObjectWarning, match="missing required arguments"):
        assert obj.args_valid("osc", [], arg_info) is False

    with pytest.warns(
        UnknownObjectWarning, match="bad type\\(s\\) for required arguments"
    ):
        assert obj.args_valid("osc", ["bad"], arg_info) is False

    with pytest.warns(
        UnknownObjectWarning, match="bad type\\(s\\) for optional arguments"
    ):
        assert obj.args_valid("osc", [440, "bad"], strict_optional) is False


def test_get_typed_args_converts_numeric_and_keeps_symbolic() -> None:
    """Verify conversion preserves numeric and symbolic text values."""
    obj = MaxObject("button")
    assert obj.get_typed_args(["7", "7.5", "name"]) == [7, 7.5, "name"]
