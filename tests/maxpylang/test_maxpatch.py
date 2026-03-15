"""Tests for patch-level operations."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from _pytest.capture import CaptureFixture
    from _pytest.monkeypatch import MonkeyPatch

import pytest

from maxpylang import MaxPatch
from maxpylang.exceptions import UnknownObjectWarning

_UNKNOWN_OBJ_NAME = "definitely_unknown"

_GRID_SPACING = [50, 60]
_CUSTOM_SPACING = [[10, 20]]
_PATCH_CANVAS_X = 400
_DEFAULT_VERTICAL_COUNT = 2


def write_js(tmp_path: Path, name: str = "demo.js", text: str | None = None) -> Path:
    """Write a js fixture used for linking tests."""
    path = tmp_path / name
    path.write_text(text or "inlets = 2;\noutlets = 3;\n", encoding="utf-8")
    return path


def write_abstraction(
    tmp_path: Path, name: str = "demo.maxpat", num_inlets: int = 1, num_outlets: int = 1
) -> Path:
    """Write a mock abstraction json file."""
    boxes = [{"box": {"maxclass": "inlet"}} for _ in range(num_inlets)] + [
        {"box": {"maxclass": "outlet"}} for _ in range(num_outlets)
    ]
    path = tmp_path / name
    path.write_text(
        json.dumps(
            {
                "patcher": {
                    "boxes": boxes,
                    "lines": [],
                    "rect": [0, 0, _PATCH_CANVAS_X, 400],
                }
            }
        ),
        encoding="utf-8",
    )
    return path


def test_maxpatch_end_to_end_flow(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    """Run an end-to-end workflow touching major patch operations."""
    monkeypatch.chdir(tmp_path)
    write_js(tmp_path)
    write_abstraction(tmp_path)

    patch = MaxPatch(verbose=False)
    patch.set_position("bad", 1)
    patch.set_position(0, 0)

    grid_objs = patch.place(
        "toggle", "button", spacing_type="grid", spacing=[50, 60], verbose=True
    )
    custom_objs = patch.place(
        "message hello", spacing_type="custom", spacing=[[10, 20]], verbose=True
    )
    vertical_objs = patch.place(
        "toggle",
        "button",
        spacing_type="vertical",
        spacing=30,
        starting_pos=[0, 0],
        verbose=True,
    )
    random_objs = patch.place(
        "toggle",
        "button",
        randpick=True,
        num_objs=[2],
        seed=1,
        weights=[0.5, 0.5],
        spacing_type="random",
        verbose=True,
    )
    js_obj = patch.place(
        "js demo", spacing_type="custom", spacing=[[30, 40]], verbose=True
    )[0]
    abs_obj = patch.place(
        "demo", spacing_type="custom", spacing=[[50, 60]], verbose=True
    )[0]
    with pytest.warns(UnknownObjectWarning, match=_UNKNOWN_OBJ_NAME):
        unknown_obj = patch.place(
            _UNKNOWN_OBJ_NAME, spacing_type="custom", spacing=[[70, 80]]
        )[0]

    patch.connect(
        [grid_objs[0].outs[0], grid_objs[1].ins[0], [[1.0, 2.0]]], verbose=True
    )
    assert patch.check_connection_typing(
        [[grid_objs[0].outs[0], grid_objs[1].ins[0]]]
    ) == [[grid_objs[0].outs[0], grid_objs[1].ins[0]]]
    assert (
        patch.check_connection_exists([[grid_objs[0].outs[0], custom_objs[0].ins[0]]])
        == []
    )

    patch.replace("obj-1", "message replaced", retain=False, verbose=True)
    patch.replace("obj-999", "message no-op", retain=False, verbose=True)

    replacement = patch.replace(
        grid_objs[0].__dict__["_dict"]["box"]["id"], "button", retain=True, verbose=True
    )
    assert replacement is None
    assert patch.objs["obj-1"].name == "button"

    patch.delete(cords=[[grid_objs[0].outs[0], grid_objs[1].ins[0]]], verbose=True)
    patch.delete(objs=["obj-2"], verbose=True)
    assert patch.curr_position == [70.0, 80.0]
    assert patch.get_unknowns()
    assert patch.get_abstractions()
    linked_js, unlinked_js = patch.get_js_objs()
    assert linked_js
    assert unlinked_js == {}
    assert patch.check("all") is None

    output = capsys.readouterr().out
    assert "Patcher: connected:" in output
    assert "objects reordered" not in output

    output_file = tmp_path / "generated.maxpat"
    patch.save(str(output_file), verbose=False)
    with pytest.warns(UnknownObjectWarning, match=_UNKNOWN_OBJ_NAME):
        reloaded = MaxPatch(load_file=str(output_file), verbose=True)
    assert reloaded.num_objs == len(reloaded.objs)
    assert reloaded.get_json()["patcher"]["boxes"]
    reloaded.reorder(verbose=False)
    reloaded.inspect("all")
    assert reloaded.inspect("all") is None

    assert len(custom_objs) == 1
    assert len(vertical_objs) == _DEFAULT_VERTICAL_COUNT
    assert len(random_objs) == _DEFAULT_VERTICAL_COUNT
    assert js_obj.name == "js"
    assert abs_obj.__dict__["_ref_file"] == "abstraction"
    assert unknown_obj.notknown() is True


def test_maxpatch_dict_property_and_default_place_obj_position() -> None:
    """Verify dict access and default placement on new object insertion."""
    patch = MaxPatch(verbose=False)

    assert isinstance(patch.dict, dict)

    placed = patch.place_obj("toggle", verbose=False)
    assert placed.__dict__["_dict"]["box"]["patching_rect"][:2] == [0.0, 0.0]


def test_maxpatch_wrapper_legacy_args_and_option_guards(
    tmp_path: Path,
) -> None:
    """Cover legacy positional wrappers and option-validation helpers."""
    false_flag = False
    true_flag = True
    template = tmp_path / "template.json"
    template.write_text(
        '{"patcher": {"rect": [0, 0, 120, 120], "boxes": [], "lines": []}}',
        encoding="utf-8",
    )
    patch_dict = {
        "patcher": {
            "rect": [0, 0, 120, 120],
            "boxes": [
                {
                    "box": {
                        "id": "obj-1",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [0.0, 0.0, 20.0, 20.0],
                        "text": "toggle",
                        "outlettype": [""],
                    }
                }
            ],
            "lines": [],
        }
    }
    input_file = tmp_path / "input.maxpat"
    input_file.write_text(json.dumps(patch_dict), encoding="utf-8")

    with pytest.raises(TypeError, match="verbose must be a bool"):
        MaxPatch(verbose="bad")
    with pytest.raises(TypeError, match="seed must be an int or None"):
        MaxPatch(verbose=False).place("toggle", seed="bad")
    with pytest.raises(TypeError, match="unexpected keyword arguments: extra"):
        MaxPatch(verbose=False).load_template(str(template), extra=True)

    with pytest.raises(TypeError, match="at most two legacy positional flags"):
        MaxPatch(None, None, true_flag, false_flag, true_flag)

    patch = MaxPatch(str(template), None, false_flag, false_flag)
    patch.load_template(str(template), false_flag)
    patch.load_file(str(input_file), false_flag, false_flag)
    patch.load_objs_from_dict(patch_dict, false_flag)
    patch.load_patchcords_from_dict({"patcher": {"boxes": [], "lines": []}}, false_flag)
    patch.reorder(true_flag)
    patch.set_position(1, 2, false_flag, false_flag)
    patch.place_check_args(
        ("toggle",),
        false_flag,
        1,
        None,
        None,
        "grid",
        [1, 1],
        None,
    )
    patch.place_pick_objs(("toggle",), false_flag, 1, None, None, false_flag)
    patch.place_grid(["toggle"], [10, 10], true_flag)
    patch.place_random(["toggle"], 1, true_flag)
    patch.place_custom(["toggle"], [[3, 4]], true_flag)
    patch.place_vertical(["toggle"], 5, true_flag)
    patch.place_obj("toggle", None, true_flag, "obj-9")
    patch.delete(None, None, false_flag)
    patch.replace("obj-9", "button", false_flag, true_flag)
    patch.save(str(tmp_path / "out.maxpat"), false_flag, false_flag)

    with pytest.raises(TypeError, match="load_file accepts at most two legacy"):
        patch.load_file(str(input_file), false_flag, false_flag, false_flag)
    with pytest.raises(TypeError, match="set_position accepts at most two legacy"):
        patch.set_position(0, 0, false_flag, false_flag, false_flag)
    with pytest.raises(TypeError, match="replace accepts at most two legacy"):
        patch.replace("obj-9", "toggle", false_flag, false_flag, false_flag)
    with pytest.raises(TypeError, match="save accepts at most two legacy"):
        patch.save(str(tmp_path / "bad.maxpat"), false_flag, false_flag, false_flag)
    with pytest.raises(
        TypeError,
        match="too many positional arguments for place_check_args",
    ):
        patch.place_check_args(("toggle",), 1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(
        TypeError,
        match="too many positional arguments for place_pick_objs",
    ):
        patch.place_pick_objs(("toggle",), 1, 2, 3, 4, 5, 6)
    with pytest.raises(TypeError, match="place_obj accepts at most two legacy"):
        patch.place_obj("toggle", None, false_flag, "obj-10", "extra")
