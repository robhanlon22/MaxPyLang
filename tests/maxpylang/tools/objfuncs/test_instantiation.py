"""Tests for objfuncs.instantiation helpers."""

import json

from maxpylang import MaxObject
from maxpylang.tools.objfuncs import instantiation as obj_instantiation


def test_build_from_specs_marks_unknown_when_validation_fails():
    updated = []

    class DummyBuildObject:
        unknown_obj_dict = {"box": {"text": "UNK"}}

        def parse_text(self, text):
            return "demo", [1], {}

        def get_ref(self, name):
            return "ref.json"

        def get_info(self, ref_file=None):
            return {
                "args": {},
                "attribs": [],
                "default": {"box": {"text": "ok"}},
                "in/out": {},
            }

        def args_valid(self, name, args, arg_info):
            return False

        def update_text(self):
            updated.append(True)

    build_obj = DummyBuildObject()
    obj_instantiation.build_from_specs(build_obj, "demo 1", {})
    assert build_obj._ref_file is None
    assert build_obj._dict == build_obj.unknown_obj_dict
    assert updated == [True]


def test_build_from_specs_declares_abstraction_without_file_lookup():
    obj = MaxObject("my_declared_abs 1 2", abstraction=True, inlets=2, outlets=3)
    assert obj._ref_file == "abstraction"
    assert obj._ext_file == "my_declared_abs.maxpat"
    assert obj._dict["box"]["numinlets"] == 2
    assert obj._dict["box"]["numoutlets"] == 3
    assert obj._dict["box"]["text"] == "my_declared_abs 1 2"


def test_build_from_dict_abstraction_path_reads_local_maxpat(tmp_path, monkeypatch):
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

    assert obj._ref_file == "abstraction"
    assert obj._ext_file == "demo.maxpat"
    assert len(obj.ins) == 1
    assert len(obj.outs) == 1


def test_build_from_dict_with_ui_maxclass_uses_existing_object_name():
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
    assert obj._dict["box"]["maxclass"] == "toggle"
