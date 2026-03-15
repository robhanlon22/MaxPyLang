"""Tests for xlet primitives."""

from types import SimpleNamespace

from maxpylang.xlet import Inlet, Outlet, _parent_name


def test_xlet_properties_and_repr_include_connected_midpoints() -> None:
    """Verify xlet property access and repr include live connection details."""
    source_parent = SimpleNamespace(__dict__={"_name": "source"})
    dest_parent = SimpleNamespace(__dict__={"_name": "dest"})
    outlet = Outlet(source_parent, 1, types=["signal"])
    inlet = Inlet(
        dest_parent, 0, sources=[outlet], midpoints=[[1.0, 2.0]], types=["signal"]
    )
    outlet.__dict__["_destinations"] = [inlet]

    assert inlet.parent is dest_parent
    assert inlet.sources == [outlet]
    assert inlet.midpoints == [[1.0, 2.0]]
    assert inlet.types == ["signal"]
    assert inlet.index == 0
    assert "midpoints" in repr(inlet)
    assert outlet.__dict__["_destinations"] == [inlet]
    assert outlet.types == ["signal"]
    assert outlet.index == 1
    assert repr(outlet) == (
        "source: outlet 1, types output: ['signal']\n"
        "\tdestination: dest: inlet 0, midpoints: [1.0, 2.0]"
    )


def test_xlet_repr_omits_midpoints_when_connection_has_none() -> None:
    """Verify repr omits midpoint rendering if list contains None."""
    source_parent = SimpleNamespace(_name="source")
    dest_parent = SimpleNamespace(_name="dest")
    outlet = Outlet(source_parent, 0)
    inlet = Inlet(dest_parent, 2, sources=[outlet], midpoints=[None])
    outlet.__dict__["_destinations"] = [inlet]

    assert repr(inlet) == "dest: inlet 2, types taken: []\n\tsource: source: outlet 0"
    assert (
        repr(outlet)
        == "source: outlet 0, types output: []\n\tdestination: dest: inlet 2"
    )


def test_xlet_mutators_and_parent_name_fallbacks() -> None:
    """Verify setters and fallback naming paths on xlet helpers."""
    named_parent = SimpleNamespace(_name="named")
    dict_parent = SimpleNamespace()
    dict_parent.__dict__["_name"] = "dict-parent"

    assert _parent_name(dict_parent) == "dict-parent"

    class NoName:
        def __str__(self) -> str:
            return "plain-parent"

    class DictOnlyName:
        def __init__(self) -> None:
            self.__dict__["_name"] = "dict-only"

        def __getattribute__(self, name: str) -> object:
            if name == "_name":
                raise AttributeError
            return object.__getattribute__(self, name)

    assert _parent_name(NoName()) == "plain-parent"
    assert _parent_name(DictOnlyName()) == "dict-only"

    outlet = Outlet(named_parent, 0)
    inlet = Inlet(named_parent, 1)
    inlet.add_source(outlet, [3.0, 4.0])
    outlet.add_destination(inlet)
    assert inlet.midpoint_for(outlet) == [3.0, 4.0]
    assert inlet.remove_source(outlet) == [3.0, 4.0]
    outlet.remove_destination(inlet)

    inlet.set_types("signal")
    outlet.set_types("int")
    assert inlet.types == "signal"
    assert outlet.types == "int"


def test_parent_name_supports_nested_dict_names() -> None:
    """Verify repr falls back to nested namespace `_name` values."""

    class DeepParent:
        pass

    parent = DeepParent()
    parent.__dict__ = {"__dict__": {"_name": "deep"}}
    outlet = Outlet(parent, 0)
    assert repr(outlet).startswith("deep: outlet 0")


def test_parent_name_prefers_direct_dict_entries() -> None:
    """Ensure `_parent_name` prefers `_name` in the direct namespace dictionary."""
    parent = SimpleNamespace()
    parent.__dict__["_name"] = "direct-name"

    assert _parent_name(parent) == "direct-name"


def test_parent_name_handles_custom_namespace_dicts() -> None:
    """Names stored directly in `__dict__` dictionaries should be used."""

    class DictParent:
        pass

    parent = DictParent()
    parent.__dict__ = {"_name": "dict-level"}
    assert _parent_name(parent) == "dict-level"


def test_set_types_updates_both_xlet_types() -> None:
    """Ensure `set_types` mutates the stored type information."""
    parent = SimpleNamespace(_name="parent")
    inlet = Inlet(parent, 0)
    outlet = Outlet(parent, 1)

    inlet.set_types(["bang"])
    outlet.set_types(["bang"])

    assert inlet.types == ["bang"]
    assert outlet.types == ["bang"]
