import copy
import json
import sys
from types import SimpleNamespace

import pytest

import maxpylang
from maxpylang import MaxObject, MaxPatch, importobjs
from maxpylang.exceptions import UnknownObjectWarning
from maxpylang.tools import constants, misc, typechecks
from maxpylang.xlet import Inlet, Outlet


def write_js(tmp_path, name="demo.js", text=None):
    path = tmp_path / name
    path.write_text(text or "inlets = 2;\noutlets = 3;\n")
    return path


def write_abstraction(tmp_path, name="demo.maxpat", num_inlets=1, num_outlets=1):
    boxes = [{"box": {"maxclass": "inlet"}} for _ in range(num_inlets)] + [
        {"box": {"maxclass": "outlet"}} for _ in range(num_outlets)
    ]
    path = tmp_path / name
    path.write_text(
        json.dumps({"patcher": {"boxes": boxes, "lines": [], "rect": [0, 0, 400, 400]}})
    )
    return path


def test_public_exports_and_small_utils(monkeypatch, tmp_path):
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
    assert isinstance(objects_module.toggle, MaxObject)
    assert isinstance(objects_module.cycle_tilde, MaxObject)
    assert isinstance(objects_module.jit_movie, MaxObject)
    with pytest.raises(AttributeError, match="not_real_attr"):
        getattr(maxpylang, "not_real_attr")

    constants_file = tmp_path / "constants.json"
    constants_file.write_text(
        json.dumps(
            {"packages_path": "/packages", "max_refpath": "/ref", "wait_time": 1}
        )
    )
    monkeypatch.setattr(constants, "constants_file", str(constants_file))
    constants.set_packages_path("/new/packages")
    constants.set_max_path("/Applications/Max.app")
    constants.set_wait_time(7)
    assert constants.get_constant("packages_path") == "/new/packages"
    assert constants.get_constant("max_refpath").endswith(
        "Contents/Resources/C74/docs/refpages/"
    )
    assert constants.get_constant("wait_time") == 7

    obj_info_root = tmp_path / "OBJ_INFO"
    (obj_info_root / "pkg").mkdir(parents=True)
    (obj_info_root / "pkg" / "alpha.json").write_text("{}")
    (obj_info_root / "pkg" / "beta.json").write_text("{}")
    monkeypatch.setattr(misc, "obj_info_folder", str(obj_info_root))
    assert misc.get_objs() == {"pkg": ["alpha", "beta"]}

    assert typechecks.check_number("2.5") is True
    assert typechecks.check_number("nope") is False
    assert typechecks.check_int("2") is True
    assert typechecks.check_int("2.5") is False
    assert typechecks.check_any(object()) is True
    assert typechecks.check_type(["int", "symbol"], "3") is True
    assert typechecks.check_type(["int"], "word") is False

    parent = SimpleNamespace(_name="osc")
    outlet = Outlet(parent, 0, types=["signal"])
    inlet = Inlet(parent, 1, sources=[outlet], midpoints=[[1.0, 2.0]], types=["signal"])
    outlet._destinations = [inlet]
    assert inlet.parent is parent
    assert inlet.sources == [outlet]
    assert inlet.midpoints == [[1.0, 2.0]]
    assert inlet.types == ["signal"]
    assert inlet.index == 1
    assert "midpoints" in repr(inlet)
    assert outlet.parent is parent
    assert outlet.destinations == [inlet]
    assert outlet.types == ["signal"]
    assert outlet.index == 0
    assert "destination" in repr(outlet)


def test_importobjs_doc_and_stub_helpers(monkeypatch, tmp_path, capsys):
    rich_ref = tmp_path / "rich.maxref.xml"
    rich_ref.write_text(
        """
<c74object name="2d.wave~">
  <digest>Signal <b>digest</b></digest>
  <description>Main <i>description</i>.</description>
  <inletlist>
    <inlet id="0" type="signal">
      <digest>Signal input</digest>
    </inlet>
    <inlet id="1">
      <digest>Bang input</digest>
    </inlet>
    <inlet id="2" type="int" />
  </inletlist>
  <outletlist>
    <outlet id="0" type="signal">
      <digest>Signal output</digest>
    </outlet>
    <outlet id="1">
      <digest>Status output</digest>
    </outlet>
    <outlet id="2" type="int" />
  </outletlist>
  <methodlist>
    <method name="bang">
      <digest>Trigger now</digest>
      <description>Force output.</description>
      <arglist>
        <arg name="force" type="int" />
      </arglist>
    </method>
  </methodlist>
</c74object>
""".strip(),
        encoding="utf-8",
    )
    placeholder_ref = tmp_path / "placeholder.maxref.xml"
    placeholder_ref.write_text(
        """
<c74object name="in">
  <digest>TEXT_HERE</digest>
  <description>TEXT_HERE</description>
  <methodlist>
    <method name="noop">
      <digest>TEXT_HERE</digest>
      <description>TEXT_HERE</description>
    </method>
  </methodlist>
</c74object>
""".strip(),
        encoding="utf-8",
    )

    assert importobjs.strip_xml_text(None) == ""
    assert (
        importobjs.strip_xml_text(
            importobjs.ET.fromstring("<digest>Hello <b>there</b></digest>")
        )
        == "Hello there"
    )

    doc_info = importobjs.get_obj_doc_info(
        [str(rich_ref), str(placeholder_ref)], ["2d.wave~", "in"]
    )
    assert doc_info["2d.wave~"] == {
        "digest": "Signal digest",
        "description": "Main description.",
        "inlets": [
            {"id": "0", "type": "signal", "digest": "Signal input"},
            {"id": "1", "digest": "Bang input"},
            {"id": "2", "type": "int"},
        ],
        "outlets": [
            {"id": "0", "type": "signal", "digest": "Signal output"},
            {"id": "1", "digest": "Status output"},
            {"id": "2", "type": "int"},
        ],
        "methods": [
            {
                "name": "bang",
                "digest": "Trigger now",
                "description": "Force output.",
                "args": [{"name": "force", "type": "int"}],
            }
        ],
    }
    assert doc_info["in"] == {"methods": [{"name": "noop"}]}

    assert importobjs.sanitize_py_name("2d.wave~") == "_2d_wave_tilde"
    assert importobjs.sanitize_py_name("in") == "in_"
    assert importobjs.sanitize_py_name("live.dial") == "live_dial"

    rich_obj_info = {
        "doc": doc_info["2d.wave~"],
        "args": {
            "required": [{"name": "freq", "type": ["number", "int"]}],
            "optional": [{"name": "label", "type": "symbol"}],
        },
        "attribs": [{"name": "COMMON"}, {"name": "gain"}],
    }
    docstring = importobjs._build_docstring("2d.wave~", rich_obj_info)
    assert "2d.wave~ - Signal digest" in docstring
    assert "Main description." in docstring
    assert "freq (number, int, required)" in docstring
    assert "label (symbol, optional)" in docstring
    assert "0 (signal): Signal input" in docstring
    assert "1: Bang input" in docstring
    assert "2 (int)" in docstring
    assert "Messages: bang" in docstring
    assert "Attributes: gain" in docstring
    assert (
        importobjs._build_docstring("plain", {"doc": {}, "args": {}, "attribs": []})
        == "plain"
    )

    fake_module = tmp_path / "generated_pkg" / "importobjs.py"
    fake_module.parent.mkdir(parents=True)
    fake_module.write_text("# stub target", encoding="utf-8")
    monkeypatch.setattr(importobjs, "__file__", str(fake_module))

    info_root = tmp_path / "info"
    demo_info = info_root / "demo"
    empty_info = info_root / "empty"
    demo_info.mkdir(parents=True)
    empty_info.mkdir(parents=True)
    (demo_info / "2d.wave~.json").write_text(
        json.dumps(rich_obj_info),
        encoding="utf-8",
    )
    (demo_info / "in.json").write_text(
        json.dumps({"doc": {"methods": [{"name": "noop"}]}, "args": {}, "attribs": []}),
        encoding="utf-8",
    )

    importobjs.generate_stubs({}, {"demo": str(demo_info), "empty": str(empty_info)})

    objects_dir = fake_module.parent / "objects"
    stub_text = (objects_dir / "demo.py").read_text(encoding="utf-8")
    init_text = (objects_dir / "__init__.py").read_text(encoding="utf-8")
    output = capsys.readouterr().out
    assert "stub module generated: objects/demo.py (2 objects)" in output
    assert "stub generation complete" in output
    assert "__all__ = [" in stub_text
    assert "'_2d_wave_tilde'" in stub_text
    assert "'in_'" in stub_text
    assert "2d.wave~ - Signal digest" in stub_text
    assert "MaxObject('2d.wave~')" in stub_text
    assert "MaxObject('in')" in stub_text
    assert "# ruff: noqa: F403" in init_text
    assert 'warnings.simplefilter("ignore", UnknownObjectWarning)' in init_text
    assert "from .demo import *" in init_text


def test_maxobject_helpers_and_validation(capsys):
    obj = MaxObject("toggle")
    obj.move(10, 20)
    assert obj._dict["box"]["patching_rect"][:2] == [10, 20]
    assert obj.check_aliases("sel") == "select"
    assert obj.get_ref("toggle").endswith("toggle.json")
    assert obj.get_info()["default"]["box"]["maxclass"] == "toggle"
    assert obj.notknown() is False
    assert repr(obj) == "toggle [toggle]"

    with pytest.warns(UnknownObjectWarning, match="does_not_exist"):
        unknown = MaxObject("does_not_exist 1")
    assert unknown.notknown() is True
    assert unknown._dict["box"]["text"] == "does_not_exist 1"
    assert repr(unknown) == "does_not_exist [does_not_exist 1]"

    name, args, text_attribs = obj.parse_text("message 1 2.5 @foo bar baz @empty")
    assert (name, args, text_attribs) == (
        "message",
        [1, 2.5],
        {"foo": ["bar", "baz"], "empty": []},
    )
    assert obj.get_typed_args(["1", "2.5", "name"]) == [1, 2.5, "name"]

    arg_info = {
        "required": [{"name": "count", "type": ["int"]}],
        "optional": [{"name": "label", "type": ["symbol"]}],
    }
    strict_optional = {
        "required": [{"name": "count", "type": ["int"]}],
        "optional": [{"name": "count2", "type": ["int"]}],
    }
    assert obj.args_valid("demo", [1, "ok"], arg_info) is True
    with pytest.warns(UnknownObjectWarning, match="missing required arguments"):
        assert obj.args_valid("demo", [], arg_info) is False
    with pytest.warns(
        UnknownObjectWarning, match="bad type\\(s\\) for required arguments"
    ):
        assert obj.args_valid("demo", ["bad"], arg_info) is False
    with pytest.warns(
        UnknownObjectWarning, match="bad type\\(s\\) for optional arguments"
    ):
        assert obj.args_valid("demo", [1, "bad"], strict_optional) is False
    assert "(arg_warning): demo" in capsys.readouterr().out

    cleaned = obj.remove_bad_attribs(
        {
            "good": [1],
            "noval": [],
            "bad": [1],
            "small": [1],
            "wrong": ["x"],
        },
        [
            {"name": "good", "type": "int", "size": "1"},
            {"name": "small", "type": "int", "size": "2"},
            {"name": "wrong", "type": "int", "size": "1"},
        ],
    )
    assert cleaned == {"good": [1], "noval": []}

    text_attrs, extra_attribs = obj.get_all_valid_attribs(
        {"bgcolor": [0, 0, 0, 1]},
        {"patching_rect": [1, 2, 3, 4], "presentation": 1},
        [{"name": "COMMON"}],
    )
    assert text_attrs == {}
    assert extra_attribs["patching_rect"] == [1, 2, 3, 4]
    assert extra_attribs["presentation"] == 1

    obj.add_extra_attribs({"presentation": 1})
    assert obj.get_extra_attribs()["presentation"] == 1

    other = SimpleNamespace(get_extra_attribs=lambda: {"presentation": 2})
    called = {}

    def fake_edit(**kwargs):
        called.update(kwargs)

    obj.edit = fake_edit
    obj.retain_attribs(other)
    assert called == {"presentation": 2}


def test_js_and_abstraction_flows(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    write_js(tmp_path)
    write_abstraction(tmp_path)

    js_obj = MaxObject("js demo")
    assert js_obj._ext_file == str(tmp_path / "demo.js")
    assert js_obj._args == [3, 2, "demo.js"]
    assert len(js_obj.ins) == 2
    assert len(js_obj.outs) == 3
    js_obj.link()
    assert "no filename specified" not in capsys.readouterr().out
    js_obj.link("demo.js")
    assert js_obj._ext_file == str(tmp_path / "demo.js")

    no_filename = MaxObject("js")
    assert no_filename._args == []
    assert "no filename specified" in capsys.readouterr().out

    js_from_dict = MaxObject(copy.deepcopy(js_obj._dict), from_dict=True)
    assert js_from_dict._args == [2, 3, "demo.js"]
    missing_js_dict = copy.deepcopy(js_obj._dict)
    missing_js_dict["box"]["saved_object_attributes"]["filename"] = "missing.js"
    missing_js = MaxObject(missing_js_dict, from_dict=True)
    assert missing_js._args == [2, 3, "missing.js"]

    abs_obj = MaxObject("demo @hidden 1")
    assert abs_obj._ext_file == "demo.maxpat"
    assert len(abs_obj.ins) == 1
    assert len(abs_obj.outs) == 1

    with pytest.warns(UnknownObjectWarning, match="mystery"):
        unknown = MaxObject("mystery")
    unknown.link("demo.maxpat")
    assert unknown._ref_file == "abstraction"
    assert unknown.name == "demo"

    with pytest.warns(UnknownObjectWarning, match="still_missing"):
        unknown_missing = MaxObject("still_missing")
    unknown_missing.link("missing.maxpat")
    assert unknown_missing._ext_file is None

    not_linkable = MaxObject("toggle")
    not_linkable.link("demo.maxpat")

    abs_dict = {
        "box": {
            "id": "obj-1",
            "maxclass": "newobj",
            "text": "demo",
            "numinlets": 1,
            "numoutlets": 1,
            "patching_rect": [0, 0, 30, 20],
        }
    }
    abs_from_dict = MaxObject(abs_dict, from_dict=True)
    assert abs_from_dict._ext_file == "demo.maxpat"
    assert len(abs_from_dict.ins) == 1
    assert len(abs_from_dict.outs) == 1


def test_declared_abstraction_skips_file_lookup_and_builds_common_attrs():
    declared = MaxObject(
        "my_declared_abs 1 2",
        abstraction=True,
        inlets=2,
        outlets=3,
        bgcolor=[1, 2, 3, 4],
    )

    assert declared._ref_file == "abstraction"
    assert declared._ext_file == "my_declared_abs.maxpat"
    assert declared.name == "my_declared_abs"
    assert declared._dict["box"]["numinlets"] == 2
    assert declared._dict["box"]["numoutlets"] == 3
    assert declared._dict["box"]["outlettype"] == ["", "", ""]
    assert declared._dict["box"]["patching_rect"] == [0.0, 0.0]
    assert len(declared.ins) == 2
    assert len(declared.outs) == 3
    assert declared._dict["box"]["bgcolor"] == [1, 2, 3, 4]
    assert declared.get_text() == "my_declared_abs 1 2"


def test_special_object_types_and_ui_build_from_dict():
    trigger = MaxObject("trigger b i 3 f s foo")
    assert trigger.get_trigger_out_types() == ["bang", "int", "int", "float", "", "foo"]

    unpack = MaxObject("unpack i 3 f foo")
    assert unpack.get_unpack_out_types() == ["int", "int", "float", ""]

    vst = MaxObject("vst~ 4 plugin")
    assert len(vst.outs) == 10
    assert vst._dict["box"]["save"][-4:] == [0, 4, "plugin", ";"]

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
    ui_obj = MaxObject(ui_dict, from_dict=True)
    assert ui_obj.name == "toggle"
    assert repr(ui_obj) == "toggle [toggle]"
    assert ui_obj.inspect() is None


def test_maxpatch_flow(monkeypatch, tmp_path):
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
    with pytest.warns(UnknownObjectWarning, match="definitely_unknown"):
        unknown_obj = patch.place(
            "definitely_unknown", spacing_type="custom", spacing=[[70, 80]]
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
    patch.delete(cords=[[grid_objs[0].outs[0], grid_objs[1].ins[0]]], verbose=True)
    patch.delete(objs=["obj-2"], verbose=True)

    assert patch.get_unknowns()
    assert patch.get_abstractions()
    linked_js, unlinked_js = patch.get_js_objs()
    assert linked_js
    assert unlinked_js == {}
    assert patch.check("all") is None
    assert patch.inspect("all") is None

    output_file = tmp_path / "generated.maxpat"
    patch.save(str(output_file), verbose=False)
    with pytest.warns(UnknownObjectWarning, match="definitely_unknown"):
        reloaded = MaxPatch(load_file=str(output_file), verbose=True)
    assert reloaded.num_objs == len(reloaded.objs)
    assert reloaded.get_json()["patcher"]["boxes"]
    reloaded.reorder(verbose=True)
    barebones_before = len(reloaded._patcher_dict["patcher"]["boxes"])
    reloaded.add_barebones_obj("cycle~")
    assert len(reloaded._patcher_dict["patcher"]["boxes"]) == barebones_before + 1

    assert len(custom_objs) == 1
    assert len(vertical_objs) == 2
    assert len(random_objs) == 2
    assert js_obj.name == "js"
    assert abs_obj._ref_file == "abstraction"
    assert unknown_obj.notknown() is True


def test_patch_helper_branches():
    patch = MaxPatch(verbose=False)

    assert patch.place_check_args(
        ("toggle",), False, None, None, None, "grid", [10, 20], [1, 2]
    ) == (
        1,
        [1, 2],
    )
    assert (
        patch.place_check_args(
            ("toggle",), True, None, None, None, "random", [10, 20], None
        )[0]
        == 1
    )

    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, [1, 2], None, None, "grid", [10, 20], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, 1, None, None, "vertical", [10, 20], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, 1, None, None, "bogus", [10, 20], None
        )

    assert patch.place_pick_objs(["toggle"], False, 2, None, None, False) == [
        "toggle",
        "toggle",
    ]
    picked = patch.place_pick_objs(["toggle", "button"], True, 2, 1, [0.5, 0.5], True)
    assert len(picked) == 2

    with pytest.raises(AssertionError):
        patch.check_connection_format([["bad", "types"]])
    with pytest.raises(AssertionError):
        patch.get_obj_from_spec(object())
