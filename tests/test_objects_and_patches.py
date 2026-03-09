import json
from types import SimpleNamespace

import pytest

from maxpylang import MaxObject, MaxPatch
from maxpylang.exceptions import UnknownObjectWarning
from maxpylang.tools.objfuncs import exposed as obj_exposed
from maxpylang.tools.objfuncs import instantiation as obj_instantiation


def test_maxobject_user_methods_cover_known_and_unknown_paths(capsys):
    obj = MaxObject("cycle~ 440", color=[0.1, 0.2, 0.3, 0.4])

    assert obj.name == "cycle~"
    assert len(obj.ins) == 2
    assert len(obj.outs) == 1
    assert obj.get_text() == "cycle~ 440"
    assert obj.get_extra_attribs()["color"] == [0.1, 0.2, 0.3, 0.4]

    obj.move(12, 34)
    assert obj._dict["box"]["patching_rect"][:2] == [12, 34]

    obj.edit(text="880 @fontsize 18", text_add="replace")
    edit_output = capsys.readouterr().out
    assert "fontsize is not a valid attribute argument" in edit_output
    assert obj.get_text() == "cycle~ 880"
    assert obj.inspect() is None

    obj.debug()
    debug_output = capsys.readouterr().out
    assert "name cycle~" in debug_output

    with pytest.warns(UnknownObjectWarning, match="this_object_is_missing"):
        unknown = MaxObject("this_object_is_missing")
    assert unknown.notknown() is True
    assert "this_object_is_missing" in repr(unknown)

    unknown.edit(text="1")
    output = capsys.readouterr().out
    assert "attempting edit on empty object" in output

    obj.link()
    assert "cannot be linked to a file" in capsys.readouterr().out


def test_js_abstraction_and_build_from_dict_paths(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    js_file = tmp_path / "demo.js"
    js_file.write_text("inlets = 2;\noutlets = 3;\n", encoding="utf-8")
    abstraction_file = tmp_path / "demo.maxpat"
    abstraction_file.write_text(
        json.dumps(
            {
                "patcher": {
                    "boxes": [
                        {"box": {"maxclass": "inlet"}},
                        {"box": {"maxclass": "outlet"}},
                    ]
                }
            }
        ),
        encoding="utf-8",
    )

    js_obj = MaxObject("js demo")
    assert js_obj._ext_file == str(js_file.resolve())
    assert js_obj._args == [3, 2, "demo.js"]
    assert len(js_obj.ins) == 2
    assert len(js_obj.outs) == 3

    js_obj._ext_file = None
    js_obj.link()
    assert js_obj._ext_file == str(js_file.resolve())

    abstraction = MaxObject("demo")
    assert abstraction._ref_file == "abstraction"
    assert abstraction._ext_file == "demo.maxpat"
    assert len(abstraction.ins) == 1
    assert len(abstraction.outs) == 1

    abstraction.edit(text="demo @fontsize 20", text_add="replace", bgcolor=[1, 2, 3, 4])
    assert abstraction._dict["box"]["text"] == "demo @fontsize 20"
    assert abstraction._dict["box"]["bgcolor"] == [1, 2, 3, 4]

    abstraction.link()
    assert abstraction._ext_file == "demo.maxpat"

    from_dict_obj = MaxObject(
        {
            "box": {
                "id": "obj-1",
                "maxclass": "newobj",
                "numinlets": 1,
                "numoutlets": 1,
                "patching_rect": [0.0, 0.0, 10.0, 10.0],
                "text": "button",
                "outlettype": [""],
            }
        },
        from_dict=True,
    )
    assert from_dict_obj.name == "button"
    assert len(from_dict_obj.ins) == 1
    assert len(from_dict_obj.outs) == 1

    from_dict_js = MaxObject(
        {
            "box": {
                "id": "obj-2",
                "maxclass": "newobj",
                "numinlets": 4,
                "numoutlets": 5,
                "patching_rect": [0.0, 0.0, 10.0, 10.0],
                "text": "js demo.js",
                "saved_object_attributes": {"filename": "demo.js"},
                "outlettype": ["", "", "", "", ""],
            }
        },
        from_dict=True,
    )
    assert from_dict_js._args == [4, 5, "demo.js"]
    assert len(from_dict_js.ins) == 4
    assert len(from_dict_js.outs) == 5


def test_direct_object_helpers_cover_text_args_attribs_and_reffiles(
    tmp_path, monkeypatch, capsys
):
    obj = MaxObject("button")

    name, args, text_attribs = obj.parse_text("message 1 2.5 hello @size 3 4")
    assert name == "message"
    assert args == [1, 2.5, "hello"]
    assert text_attribs == {"size": ["3", "4"]}

    obj._name = "message"
    obj._args = [1, "hello"]
    obj._text_attribs = {"fontsize": ["12"], "style": None}
    assert obj.get_text() == " 1 hello @fontsize 12 @style"
    obj.update_text()
    assert obj._dict["box"]["text"] == " 1 hello @fontsize 12 @style"

    arg_info = {
        "required": [{"name": "freq", "type": ["number"]}],
        "optional": [{"name": "label", "type": ["symbol"]}],
    }
    strict_optional = {
        "required": [{"name": "freq", "type": ["number"]}],
        "optional": [{"name": "count", "type": ["int"]}],
    }
    assert obj.args_valid("osc", [440, "main"], arg_info) is True
    assert "args may have special reqs" in capsys.readouterr().out
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
    assert obj.get_typed_args(["7", "7.5", "name"]) == [7, 7.5, "name"]

    attrib_specs = [
        {"name": "fontsize", "type": "float", "size": 1},
        {"name": "patching_rect", "type": "float", "size": 4},
        {"name": "COMMON"},
    ]
    cleaned = obj.remove_bad_attribs(
        {
            "fontsize": 12,
            "unknown": ["x"],
            "patching_rect": [1, 2],
            "empty": [],
            "wrong_type": ["large"],
        },
        attrib_specs[:-1] + [{"name": "wrong_type", "type": "float", "size": 1}],
    )
    assert cleaned == {"fontsize": 12, "empty": []}
    attrib_output = capsys.readouterr().out
    assert "not a valid attribute argument" in attrib_output
    assert "requires 4 arguments" in attrib_output
    assert "requires arguments of type float" in attrib_output
    assert "no argument given for attribute empty" in attrib_output

    text_attribs, extra_attribs = obj.get_all_valid_attribs(
        {"fontsize": ["14"]},
        {"patching_rect": [1, 2, 3, 4], "bogus": ["x"]},
        attrib_specs,
    )
    assert text_attribs == {"fontsize": ["14"]}
    assert extra_attribs == {"patching_rect": [1, 2, 3, 4]}

    source = MaxObject("button", bgcolor=[1, 2, 3, 4])
    target = MaxObject("button")
    target.retain_attribs(source)
    assert target.get_extra_attribs()["bgcolor"] == [1, 2, 3, 4]

    ref_root = tmp_path / "obj-info"
    (ref_root / "pkg").mkdir(parents=True)
    ref_file = ref_root / "pkg" / "foo.json"
    ref_file.write_text(json.dumps({"hello": "world"}), encoding="utf-8")
    (ref_root / "obj_aliases.json").write_text(
        json.dumps({"bar": "foo"}), encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)
    (tmp_path / "demo.maxpat").write_text("{}", encoding="utf-8")
    obj.obj_info_folder = str(ref_root)
    obj.known_objs = {"pkg": ["foo"]}

    assert obj.check_aliases("bar") == "foo"
    assert obj.get_ref("bar") == str(ref_file)
    assert obj.get_ref("demo") == "abstraction"
    with pytest.warns(UnknownObjectWarning, match="still_missing"):
        assert obj.get_ref("still_missing") == "not_found"
    assert obj.get_info(ref_file=str(ref_file)) == {"hello": "world"}

    bad_edit = MaxObject("cycle~ 440")
    bad_edit.args_valid = lambda *args, **kwargs: False
    bad_edit.get_info = lambda ref_file=None: {"args": {}}
    bad_edit.edit(text="nope", text_add="replace")
    assert "not edited" in capsys.readouterr().out

    update_calls = []
    dummy = SimpleNamespace(
        parse_text=lambda text: ("demo", [], {}),
        get_ref=lambda name: "demo.json",
        get_info=lambda ref_file=None: {"args": {}},
        args_valid=lambda name, args, arg_info: False,
        unknown_obj_dict={"box": {"text": "UNK"}},
        update_text=lambda: update_calls.append("updated"),
    )
    obj_instantiation.build_from_specs(dummy, "demo", {})
    assert dummy._ref_file is None
    assert dummy._dict == {"box": {"text": "UNK"}}
    assert update_calls == ["updated"]


def test_makexlets_helpers_cover_dynamic_io_updates(capsys):
    obj = MaxObject("button")
    obj._dict["box"]["numinlets"] = 1
    obj._dict["box"]["numoutlets"] = 2
    obj._dict["box"]["outlettype"] = ["", "signal"]
    obj.make_xlets_from_self_dict()
    assert len(obj.ins) == 1
    assert [outlet.types for outlet in obj.outs] == ["any", "signal"]

    obj._args = [5, "x", 3]
    assert (
        obj.parse_io_num(
            [{"argtype": "n", "index": "all", "add_amt": 1}],
            default_num=0,
        )
        == 3
    )
    assert (
        obj.parse_io_num(
            [
                {
                    "argtype": "any",
                    "index": 0,
                    "acc_vals": [1, 4, 8],
                    "comparitor": "> 0",
                }
            ],
            default_num=0,
        )
        == 4
    )
    assert (
        obj.parse_io_num(
            [{"argtype": "any", "index": 99}],
            default_num=7,
        )
        == 7
    )
    assert (
        obj.parse_io_num(
            [{"argtype": "any", "index": 0, "comparitor": "< 0"}],
            default_num=9,
        )
        == 9
    )

    trigger = MaxObject("button")
    trigger._args = ["b", "i", "3.5", "s", "custom"]
    assert trigger.get_trigger_out_types() == ["bang", "int", "float", "", "custom"]
    assert trigger.get_unpack_out_types() == ["", "int", "float", "", ""]
    assert trigger.parse_io_typing("trigger_out", 5) == [
        "bang",
        "int",
        "float",
        "",
        "custom",
    ]
    assert trigger.parse_io_typing("unpack_out", 5) == [
        "",
        "int",
        "float",
        "",
        "",
    ]
    assert trigger.parse_io_typing(None, 2) == [None, None]
    assert trigger.parse_io_typing(
        {"default": "any", "first": [1, "int"], "last": [1, "float"]},
        3,
    ) == ["int", "any", "float"]

    typed = MaxObject("button")
    typed._dict["box"]["numinlets"] = 1
    typed._dict["box"]["numoutlets"] = 1
    typed._dict["box"]["outlettype"] = [""]
    typed.make_xlets_from_self_dict()
    typed.update_xlet_typing(
        {"numinlets": [{"type": {"default": "signal"}}]},
        "numinlets",
        1,
    )
    typed.update_xlet_typing(
        {"numoutlets": [{"type": {"default": "", "last": [1, "float"]}}]},
        "numoutlets",
        1,
    )
    assert typed.ins[0].types == "signal"
    assert typed.outs[0].types == "float"
    assert typed._dict["box"]["outlettype"] == ["float"]

    patch = MaxPatch(verbose=False)
    left = patch.place("toggle", verbose=False)[0]
    right = patch.place("number", verbose=False)[0]
    patch.connect([left.outs[0], right.ins[0]], verbose=False)

    dynamic = MaxObject("button")
    dynamic.add_xlets(1, "numinlets")
    dynamic.add_xlets(1, "numoutlets")
    assert len(dynamic.ins) == 2
    assert len(dynamic.outs) == 2

    connected = MaxObject("button")
    connected._ins = [right.ins[0]]
    connected._outs = [left.outs[0]]
    connected.remove_xlets(1, "numinlets")
    connected.remove_xlets(1, "numoutlets")
    removal_output = capsys.readouterr().out
    assert "Patchcord removed" in removal_output

    shrinking = MaxObject("button")
    shrinking._dict["box"]["numoutlets"] = 2
    shrinking._dict["box"]["outlettype"] = ["", ""]
    shrinking.make_xlets_from_self_dict()
    shrinking._args = [0]
    shrinking._outs[1]._destinations = [right.ins[0]]
    right.ins[0]._sources = [shrinking._outs[1]]
    right.ins[0]._midpoints = [[None]]
    shrinking.update_vst = lambda: None
    shrinking.update_ins_outs(
        {"numoutlets": [{"argtype": "any", "index": 0, "type": {"default": ""}}]},
        default_info={},
    )
    assert shrinking._dict["box"]["numoutlets"] == 0

    typed._args = [2]
    typed._name = "vst~"
    typed._dict["box"]["save"] = ["prefix", ";"]
    typed.update_vst = MaxObject.update_vst.__get__(typed, MaxObject)
    typed.update_ins_outs(
        {
            "numoutlets": [
                {
                    "argtype": "any",
                    "index": 0,
                    "type": {"default": "", "first": [1, "int"]},
                }
            ]
        },
        default_info={},
    )
    assert typed._dict["box"]["numoutlets"] == 2
    assert typed._dict["box"]["save"] == ["prefix", 2, ";"]


def test_maxpatch_and_patch_helpers_cover_user_flows(tmp_path, capsys):
    patch = MaxPatch(template="empty_template.json", verbose=True)
    assert patch.num_objs == 0
    assert patch.objs == {}
    assert patch.curr_position == [0.0, 0.0]
    assert isinstance(patch.dict, dict)

    patch.set_position("bad", 1, from_place=True, verbose=True)
    assert "starting position must be specified" in capsys.readouterr().out
    patch.set_position(5, 6, verbose=True)
    assert patch.curr_position == [5, 6]

    with pytest.raises(AssertionError):
        patch.place_check_args(("button",), False, 1, None, None, "grid", "bad", None)
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button", "toggle"), True, 1, None, [1.0], "grid", [1, 1], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button",), False, 1, None, None, "diagonal", [1, 1], None
        )

    num_objs, starting_pos = patch.place_check_args(
        ("button", "toggle"),
        True,
        [3],
        None,
        [0.5, 0.5],
        "random",
        [1, 1],
        "bad",
    )
    assert num_objs == 3
    assert starting_pos is None
    assert "starting position must be [x, y]" in capsys.readouterr().out

    grid = patch.place(
        "button",
        "toggle",
        num_objs=[1, 2],
        spacing_type="grid",
        spacing=[10, 10],
        verbose=False,
    )
    assert len(grid) == 3

    custom = patch.place(
        "number", spacing_type="custom", spacing=[[1, 2]], verbose=False
    )
    assert custom[0]._dict["box"]["patching_rect"][:2] == [1, 2]

    vertical = patch.place(
        "message", spacing_type="vertical", spacing=15, verbose=False
    )
    assert vertical[0]._dict["box"]["patching_rect"][1] == patch.curr_position[1]

    random_objs = patch.place(
        "button",
        "toggle",
        randpick=True,
        num_objs=[2],
        seed=1,
        spacing_type="random",
        verbose=False,
    )
    assert len(random_objs) == 2
    seeded_in_place = patch.place(
        "button",
        randpick=True,
        num_objs=1,
        seed=None,
        weights=[1.0],
        spacing_type="random",
        verbose=False,
    )
    assert len(seeded_in_place) == 1
    random_without_seed = patch.place_pick_objs(
        ["button", "toggle"], True, 2, None, [0.5, 0.5], False
    )
    assert len(random_without_seed) == 2
    custom_counts, custom_positions = patch.place_check_args(
        ("button", "toggle"),
        False,
        [1, 2],
        None,
        None,
        "custom",
        [[1, 1], [2, 2], [3, 3]],
        None,
    )
    assert custom_counts == [1, 2]
    assert custom_positions is None
    rand_custom_counts, _ = patch.place_check_args(
        ("button", "toggle"),
        True,
        2,
        None,
        [0.5, 0.5],
        "custom",
        [[1, 1], [2, 2]],
        None,
    )
    assert rand_custom_counts == 2

    patch.connect([grid[0].outs[0], custom[0].ins[0], [1.0, 2.0]], verbose=True)
    assert patch.check_connection_typing([[grid[0].outs[0], custom[0].ins[0]]]) == [
        [grid[0].outs[0], custom[0].ins[0]]
    ]
    assert patch.check_connection_exists([[grid[0].outs[0], custom[0].ins[0]]]) == [
        [grid[0].outs[0], custom[0].ins[0]]
    ]
    assert (
        patch.check_connection_exists([[vertical[0].outs[0], custom[0].ins[0]]]) == []
    )
    assert "not connected to" in capsys.readouterr().out

    with pytest.raises(AssertionError):
        patch.check_connection_format([("bad", "bad")])

    patch.replace("missing", "button")
    assert "nothing changed" in capsys.readouterr().out

    replacement = patch.replace(
        grid[0]._dict["box"]["id"], "button", retain=True, verbose=False
    )
    assert replacement is None
    assert patch.objs["obj-1"].name == "button"

    cords = patch.delete_get_extra_cords("obj-1")
    assert cords
    patch.delete(
        objs=["missing", "obj-1"],
        cords=[[grid[1].outs[0], custom[0].ins[0]]],
        verbose=True,
    )
    delete_output = capsys.readouterr().out
    assert "delete error: missing not in patch" in delete_output
    assert "disconnected:" in delete_output
    assert "object deleted:" in delete_output
    assert patch.num_objs == len(patch.objs)

    patch.reorder(verbose=True)
    assert "objects reordered" in capsys.readouterr().out
    assert patch.inspect("all") is None

    save_path = tmp_path / "roundtrip.maxpat"
    patch.save(save_path.as_posix(), verbose=False, check=False)
    loaded = MaxPatch(load_file=save_path.as_posix(), verbose=False)
    assert loaded.num_objs == len(loaded.objs)

    wrap_patch = MaxPatch(verbose=False)
    wrap_patch._patcher_dict["patcher"]["rect"][2] = 15
    wrap_patch.place_grid(["button", "toggle"], [10, 10], verbose=False)
    assert wrap_patch.curr_position == [10.0, 30.0]

    unknown_patch = MaxPatch(verbose=False)
    with pytest.warns(UnknownObjectWarning, match="not-a-real-object"):
        unknown_patch.place("not-a-real-object", verbose=True)
    assert "(unknown) added" in capsys.readouterr().out

    swap_patch = MaxPatch(verbose=False)
    old = swap_patch.place("toggle", verbose=False)[0]
    source = swap_patch.place("number", verbose=False)[0]
    destination = swap_patch.place("message hello", verbose=False)[0]
    swap_patch.connect(
        [source.outs[0], old.ins[0]], [old.outs[0], destination.ins[0]], verbose=False
    )
    new = MaxObject("button")
    swap_patch.swap_patchcords(new, old)
    assert source.outs[0].destinations[0].parent is new
    assert new.outs[0].destinations[0].parent is destination


def test_patch_instantiation_helpers_cover_template_and_cleaning(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    template = template_dir / "simple.json"
    template.write_text(
        json.dumps({"patcher": {"rect": [0, 0, 100, 100], "boxes": [], "lines": []}}),
        encoding="utf-8",
    )

    patch = MaxPatch(verbose=False)
    patch.patch_templates_path = str(template_dir)
    patch.load_template("simple.json", verbose=False)
    assert patch._patcher_dict["patcher"]["rect"] == [0, 0, 100, 100]

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
                        "patching_rect": [1.0, 2.0, 3.0, 4.0],
                        "text": "button",
                        "outlettype": [""],
                    }
                },
                {
                    "box": {
                        "id": "obj-2",
                        "maxclass": "newobj",
                        "numinlets": 1,
                        "numoutlets": 1,
                        "patching_rect": [5.0, 6.0, 7.0, 8.0],
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

    patch.load_objs_from_dict(patch_dict, verbose=False)
    assert sorted(patch.objs) == ["obj-1", "obj-2"]

    patch.load_patchcords_from_dict(patch_dict, verbose=False)
    assert patch.objs["obj-1"].outs[0].destinations == [patch.objs["obj-2"].ins[0]]

    cleaned = patch.clean_patcher_dict(json.loads(json.dumps(patch_dict)))
    assert cleaned["patcher"]["boxes"] == []
    assert cleaned["patcher"]["lines"] == []


def test_direct_helper_branch_coverage_paths(tmp_path, capsys):
    class DummyEditObject:
        name = "demo"
        _ref_file = "ref.json"
        _args = []
        _text_attribs = {}
        _dict = {"box": {"text": "demo"}}

        def notknown(self):
            return False

        def parse_text(self, text):
            return "demo", [1], {}

        def get_info(self):
            return {"args": {}, "attribs": [], "in/out": {}, "default": {}}

        def args_valid(self, name, args, arg_info):
            return False

    obj_exposed.edit(DummyEditObject(), text="1", text_add="replace")
    assert "demo not edited" in capsys.readouterr().out

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

    patch = MaxPatch(verbose=False)
    patch._patcher_dict["patcher"]["rect"][2] = 15
    grid = patch.place(
        "toggle", "button", spacing_type="grid", spacing=[10, 10], verbose=False
    )
    assert len(grid) == 2
    assert patch.curr_position[1] >= 20

    assert patch.place_check_args(
        ("toggle",),
        False,
        [2],
        None,
        None,
        "custom",
        [[1, 2], [3, 4]],
        None,
    )[0] == [2]
    assert (
        patch.place_check_args(
            ("toggle",),
            True,
            2,
            None,
            None,
            "custom",
            [[1, 2], [3, 4]],
            None,
        )[0]
        == 2
    )

    picked = patch.place_pick_objs(["toggle"], True, 1, None, None, False)
    assert len(picked) == 1

    random_obj = patch.place("toggle", spacing_type="random", verbose=False)[0]
    assert random_obj.name == "toggle"

    with pytest.warns(UnknownObjectWarning, match="totally_unknown_object"):
        unknown = patch.place_obj("totally_unknown_object", verbose=True)
    assert unknown.notknown() is True
    assert "(unknown)" in capsys.readouterr().out

    source_patch = MaxPatch(verbose=False)
    source = source_patch.place("toggle", verbose=False)[0]
    old = source_patch.place("button", verbose=False)[0]
    dest = source_patch.place("number", verbose=False)[0]
    source_patch.connect(
        [source.outs[0], old.ins[0]], [old.outs[0], dest.ins[0]], verbose=False
    )
    replacement = MaxObject("toggle")
    source_patch.swap_patchcords(replacement, old)
    assert replacement.ins[0].sources == [source.outs[0]]
    assert replacement.outs[0].destinations == [dest.ins[0]]

    xlet_obj = MaxObject("button")
    xlet_obj.add_xlets(1, "numoutlets")
    receiver = MaxObject("number")
    receiver.ins[0]._sources.append(xlet_obj.outs[1])
    receiver.ins[0]._midpoints.append([1.0, 2.0])
    xlet_obj.outs[1]._destinations.append(receiver.ins[0])
    xlet_obj._args = [0]
    xlet_obj.update_ins_outs(
        {"numoutlets": [{"argtype": "any", "index": 0, "type": {"default": ""}}]},
        default_info={},
    )
    removal_output = capsys.readouterr().out
    assert "Patchcord removed" in removal_output
    assert xlet_obj.outs == []

    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    template = template_dir / "verbose.json"
    template.write_text(
        json.dumps({"patcher": {"rect": [0, 0, 50, 50], "boxes": [], "lines": []}}),
        encoding="utf-8",
    )
    verbose_patch = MaxPatch(verbose=False)
    verbose_patch.patch_templates_path = str(template_dir)
    verbose_patch.load_template("verbose.json", verbose=True)
    assert (
        "new patch created from template file: verbose.json" in capsys.readouterr().out
    )
