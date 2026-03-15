"""Tests for package-level exports and lazy package loading."""

import json
import sys
from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

import maxpylang
from maxpylang import MaxObject, MaxPatch

_DEFAULT_WAIT_TIME = 7


def test_public_exports_and_lazy_objects_import(
) -> None:
    """Verify package-level exports and lazy import behavior."""
    assert maxpylang.MaxObject is MaxObject
    assert maxpylang.MaxPatch is MaxPatch
    assert hasattr(maxpylang, "import_objs")
    assert hasattr(maxpylang, "constants")
    assert hasattr(maxpylang, "Inlet")
    assert hasattr(maxpylang, "Outlet")

    maxpylang.__dict__.pop("objects", None)

    for module_name in (
        "maxpylang.objects",
        "maxpylang.objects.max",
        "maxpylang.objects.msp",
        "maxpylang.objects.jit",
    ):
        sys.modules.pop(module_name, None)

    objects_module = maxpylang.objects
    assert maxpylang.objects is objects_module
    assert "maxpylang.objects" in sys.modules

    with pytest.raises(AttributeError, match="not_real_attr"):
        _ = maxpylang.not_real_attr


def test_constants_file_roundtrip_for_default_max_ref_path(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify constants are persisted and resolved back to expected paths."""
    constants_file = tmp_path / "constants.json"
    constants_file.write_text(
        json.dumps(
            {"packages_path": "/packages", "max_refpath": "/ref", "wait_time": 1},
            indent=2,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(maxpylang.constants, "constants_file", str(constants_file))

    maxpylang.constants.set_packages_path("/new/packages")
    maxpylang.constants.set_max_path("/Applications/Max.app")
    maxpylang.constants.set_wait_time(_DEFAULT_WAIT_TIME)

    assert maxpylang.constants.get_constant("packages_path") == "/new/packages"
    assert maxpylang.constants.get_constant("max_refpath").endswith(
        "Contents/Resources/C74/docs/refpages/"
    )
    assert maxpylang.constants.get_constant("wait_time") == _DEFAULT_WAIT_TIME
