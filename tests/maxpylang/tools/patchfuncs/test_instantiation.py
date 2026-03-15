"""Tests for patch load helpers."""

import copy
import json

from maxpylang import MaxPatch


def test_load_template_from_path(tmp_path, capsys):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    template = template_dir / "simple.json"
    template.write_text(
        json.dumps(
            {
                "patcher": {
                    "rect": [0, 0, 100, 100],
                    "boxes": [],
                    "lines": [],
                }
            }
        ),
        encoding="utf-8",
    )

    patch = MaxPatch(verbose=False)
    patch.patch_templates_path = str(template_dir)
    patch.load_template("simple.json", verbose=True)
    assert patch._patcher_dict["patcher"]["rect"] == [0, 0, 100, 100]
    assert (
        "Patcher: new patch created from template file: simple.json"
        in capsys.readouterr().out
    )


def test_load_objs_and_cords_from_dict():
    patch_dict = {
        "patcher": {
            "rect": [0, 0, 100, 100],
            "boxes": [
                {
                    "box": {
                        "id": "obj-1",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [1.0, 2.0, 30.0, 20.0],
                        "text": "toggle",
                        "outlettype": [""],
                    }
                },
                {
                    "box": {
                        "id": "obj-2",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [5.0, 6.0, 30.0, 20.0],
                        "text": "number",
                        "outlettype": [""],
                    }
                },
            ],
            "lines": [
                {
                    "patchline": {
                        "source": ["obj-1", 0],
                        "destination": ["obj-2", 0],
                        "midpoints": [9.0, 10.0],
                    }
                }
            ],
        }
    }

    patch = MaxPatch(verbose=False)
    patch.load_objs_from_dict(patch_dict, verbose=False)
    assert sorted(patch.objs) == ["obj-1", "obj-2"]
    assert patch._num_objs == 2

    patch.load_patchcords_from_dict(patch_dict, verbose=False)
    assert patch.objs["obj-1"].outs[0].destinations == [patch.objs["obj-2"].ins[0]]


def test_load_file_reorders_and_cleans_dict(tmp_path):
    patch_dict = {
        "patcher": {
            "rect": [0, 0, 100, 100],
            "boxes": [
                {
                    "box": {
                        "id": "obj-7",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [1.0, 2.0, 30.0, 20.0],
                        "text": "toggle",
                        "outlettype": [""],
                    }
                },
                {
                    "box": {
                        "id": "obj-3",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [5.0, 6.0, 30.0, 20.0],
                        "text": "number",
                        "outlettype": [""],
                    }
                },
            ],
            "lines": [
                {
                    "patchline": {
                        "source": ["obj-7", 0],
                        "destination": ["obj-3", 0],
                        "midpoints": [9.0, 10.0],
                    }
                }
            ],
        }
    }
    input_file = tmp_path / "from_file.maxpat"
    input_file.write_text(json.dumps(patch_dict), encoding="utf-8")

    patch = MaxPatch(verbose=False)
    patch.load_file(str(input_file), verbose=False, reorder=True)

    assert sorted(patch.objs) == ["obj-1", "obj-2"]
    assert patch._patcher_dict["patcher"]["boxes"] == []
    assert patch._patcher_dict["patcher"]["lines"] == []
    assert patch.objs["obj-1"].outs[0].destinations == [patch.objs["obj-2"].ins[0]]


def test_clean_patcher_dict_removes_boxes_and_lines():
    patch = MaxPatch(verbose=False)
    patch_dict = {
        "patcher": {
            "rect": [0, 0, 100, 100],
            "boxes": [{"box": {"text": "toggle"}}],
            "lines": [{"patchline": {"source": [0, 0], "destination": [1, 0]}}],
        }
    }
    cleaned = patch.clean_patcher_dict(copy.deepcopy(patch_dict))
    assert cleaned["patcher"]["boxes"] == []
    assert cleaned["patcher"]["lines"] == []
