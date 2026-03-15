"""Tests for objfuncs.instantiation helpers."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from _pytest.monkeypatch import MonkeyPatch

from maxpylang import MaxObject
from maxpylang.tools.objfuncs import instantiation as obj_instantiation

_ABSTRACT_INLETS = 2
_ABSTRACT_OUTLETS = 3


def test_build_from_specs_marks_unknown_when_validation_fails() -> None:
    """Verify unknown objects are kept as unknown specs."""
    updated = []
    class DummyBuildObject:
        def __init__(self) -> None:
            self.unknown_obj_dict = {"box": {"text": "UNK"}}

        def parse_text(
            self, _text: str
        ) -> tuple[str, list[str], dict[str, list[str]]]:
            return "demo", [1], {}

        def get_ref(self, _name: str) -> str:
            return "ref.json"

        def get_info(self, _ref_file: str | None = None) -> dict:
            return {
                "args": {},
                "attribs": [],
                "default": {"box": {"text": "ok"}},
                "in/out": {},
            }

        def args_valid(
            self, _name: str, _args: list[str], _arg_info: dict
        ) -> bool:
            return False

        def update_text(self) -> None:
            updated.append(True)

    build_obj = DummyBuildObject()
    obj_instantiation.build_from_specs(build_obj, "demo 1", {})
    assert build_obj.__dict__["_ref_file"] is None
    assert build_obj.__dict__["_dict"] == build_obj.unknown_obj_dict
    assert updated == [True]
    assert build_obj.__dict__["_dict"]["box"]["text"] == "UNK"
    expected_updates = 1
    assert len(updated) == expected_updates


def test_build_from_specs_declares_abstraction_without_file_lookup() -> None:
    """Verify declaration-only abstractions skip file discovery."""
    obj = MaxObject("my_declared_abs 1 2", abstraction=True, inlets=2, outlets=3)
    assert obj.__dict__["_ref_file"] == "abstraction"
    assert obj.__dict__["_ext_file"] == "my_declared_abs.maxpat"
    assert obj.__dict__["_dict"]["box"]["numinlets"] == _ABSTRACT_INLETS
    assert obj.__dict__["_dict"]["box"]["numoutlets"] == _ABSTRACT_OUTLETS
    assert obj.__dict__["_dict"]["box"]["text"] == "my_declared_abs 1 2"


def test_build_from_dict_abstraction_path_reads_local_maxpat(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify local abstractions include local maxpat path when referenced."""
    abstraction_text = {
        "patcher": {
            "boxes": [
                {"box": {"maxclass": "inlet"}},
                {"box": {"maxclass": "outlet"}},
            ]
        }
    }
    (tmp_path / "demo.maxpat").write_text(
        json.dumps(abstraction_text), encoding="utf-8"
    )
    monkeypatch.chdir(tmp_path)

    obj = MaxObject(
        {
            "box": {
                "id": "obj-1",
                "maxclass": "newobj",
                "numinlets": 1,
                "numoutlets": 1,
                "patching_rect": [0, 0, 10, 10],
                "text": "demo",
            }
        },
        from_dict=True,
    )

    assert obj.__dict__["_ref_file"] == "abstraction"
    assert obj.__dict__["_ext_file"] == "demo.maxpat"
    assert len(obj.ins) == 1
    assert len(obj.outs) == 1


def test_build_from_dict_with_ui_maxclass_uses_existing_object_name() -> None:
    """Verify ui maxclass objects preserve given names."""
    ui_dict = {
        "box": {
            "id": "obj-1",
            "maxclass": "toggle",
            "numinlets": 1,
            "numoutlets": 1,
            "outlettype": [""],
            "patching_rect": [0, 0, 20, 20],
            "text": "toggle",
        }
    }
    obj = MaxObject(ui_dict, from_dict=True)
    assert obj.name == "toggle"
    assert obj.__dict__["_dict"]["box"]["maxclass"] == "toggle"
