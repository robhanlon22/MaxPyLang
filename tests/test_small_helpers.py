import json
from pathlib import Path
from types import SimpleNamespace

from maxpylang.tools import constants
from maxpylang.tools import misc as tools_misc
from maxpylang.tools import typechecks
from maxpylang.tools.objfuncs import misc as obj_misc
from maxpylang.xlet import Inlet, Outlet


def test_typecheck_helpers_cover_numeric_and_dispatch_paths():
    assert typechecks.check_number("3.14") is True
    assert typechecks.check_number("nope") is False
    assert typechecks.check_any(object()) is True
    assert typechecks.check_int("7") is True
    assert typechecks.check_int("7.5") is False
    assert typechecks.check_type(["float"], "8.25") is True
    assert typechecks.check_type(["symbol", "int"], "hello") is True
    assert typechecks.check_type(["int"], "hello") is False


def test_get_objs_collects_sorted_json_stems_by_package(tmp_path, monkeypatch):
    package_root = tmp_path / "OBJ_INFO"
    for package, names in {"jit": ["b", "a"], "max": ["solo"]}.items():
        package_dir = package_root / package
        package_dir.mkdir(parents=True)
        for name in names:
            (package_dir / f"{name}.json").write_text("{}", encoding="utf-8")
        (package_dir / "ignore.txt").write_text("skip", encoding="utf-8")

    monkeypatch.setattr(tools_misc, "obj_info_folder", str(package_root))

    assert tools_misc.get_objs() == {"jit": ["a", "b"], "max": ["solo"]}


def test_constants_helpers_update_backing_json_file(tmp_path, monkeypatch):
    constants_file = tmp_path / "constants.json"
    constants_file.write_text(
        json.dumps(
            {
                "packages_path": "/existing/packages",
                "max_refpath": "/existing/refpages",
                "wait_time": 1,
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(constants, "constants_file", str(constants_file))

    constants.set_packages_path("/tmp/packages")
    constants.set_max_path("/Applications/Max.app")
    constants.set_wait_time(9)
    constants.set_constant("custom", "value")

    assert constants.get_constant("packages_path") == "/tmp/packages"
    assert (
        constants.get_constant("max_refpath")
        == "/Applications/Max.app/Contents/Resources/C74/docs/refpages/"
    )
    assert constants.get_constant("wait_time") == 9
    assert constants.get_constant("custom") == "value"

    persisted = json.loads(Path(constants.constants_file).read_text(encoding="utf-8"))
    assert persisted["packages_path"] == "/tmp/packages"
    assert persisted["custom"] == "value"


def test_obj_misc_helpers_cover_known_and_unknown_reprs():
    unknown = SimpleNamespace(
        _ref_file=None,
        name="cycle~",
        _dict={"box": {"text": "cycle~ 440"}},
    )
    known = SimpleNamespace(
        _ref_file="ref-file",
        name="button",
        _dict={"box": {"maxclass": "button"}},
    )

    assert obj_misc.notknown(unknown) is True
    assert obj_misc.notknown(known) is False
    assert obj_misc.__repr__(unknown) == "cycle~ [cycle~ 440]"
    assert obj_misc.__repr__(known) == "button [button]"


def test_xlet_properties_and_repr_include_connected_midpoints():
    source_parent = SimpleNamespace(_name="source")
    dest_parent = SimpleNamespace(_name="dest")
    outlet = Outlet(source_parent, 1, types=["signal"])
    inlet = Inlet(
        dest_parent, 0, sources=[outlet], midpoints=[[1.0, 2.0]], types=["signal"]
    )
    outlet._destinations = [inlet]

    assert inlet.parent is dest_parent
    assert inlet.sources == [outlet]
    assert inlet.midpoints == [[1.0, 2.0]]
    assert inlet.types == ["signal"]
    assert inlet.index == 0
    assert outlet.parent is source_parent
    assert outlet.destinations == [inlet]
    assert outlet.types == ["signal"]
    assert outlet.index == 1
    assert repr(inlet) == (
        "dest: inlet 0, types taken: ['signal']\n"
        "\tsource: source: outlet 1, midpoints: [1.0, 2.0]"
    )
    assert repr(outlet) == (
        "source: outlet 1, types output: ['signal']\n"
        "\tdestination: dest: inlet 0, midpoints: [1.0, 2.0]"
    )


def test_xlet_repr_omits_midpoints_when_connection_has_none():
    source_parent = SimpleNamespace(_name="source")
    dest_parent = SimpleNamespace(_name="dest")
    outlet = Outlet(source_parent, 0)
    inlet = Inlet(dest_parent, 2, sources=[outlet], midpoints=[None])
    outlet._destinations = [inlet]

    assert repr(inlet) == "dest: inlet 2, types taken: []\n\tsource: source: outlet 0"
    assert (
        repr(outlet)
        == "source: outlet 0, types output: []\n\tdestination: dest: inlet 2"
    )
