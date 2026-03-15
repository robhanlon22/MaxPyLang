"""Tests for xlet primitives."""

from types import SimpleNamespace

from maxpylang.xlet import Inlet, Outlet


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
