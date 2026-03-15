"""Tests for objects package export behavior."""


import maxpylang
from maxpylang import MaxObject


def test_objects_module_exports_stubs_and_is_cached() -> None:
    """Ensure objects module lazily loads package stubs and stays cached."""
    maxpylang.__dict__.pop("objects", None)
    objects_module = maxpylang.objects

    assert isinstance(objects_module.toggle, MaxObject)
    assert isinstance(objects_module.cycle_tilde, MaxObject)
    assert isinstance(objects_module.jit_movie, MaxObject)
    assert maxpylang.objects is objects_module
