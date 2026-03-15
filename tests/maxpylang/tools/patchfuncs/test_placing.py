"""Tests for patch object placement helpers."""

import pytest
from _pytest.capture import CaptureFixture

from maxpylang import MaxObject, MaxPatch
from maxpylang.exceptions import UnknownObjectWarning
from maxpylang.tools.patchfuncs import placing as placing_module

_DEFAULT_RANDOM_SEED = 1
_CANVAS_WRAP_LIMIT = 15
_WARNED_CANVAS_SIZE = [10, 10]
_KNOWN_GRID_DEFAULT = [10, 10]
_DEFAULT_RANDOM_OBJECT_COUNT = 3
_DEFAULT_CANVAS_WIDTH = 15
_CUSTOM_VERTICAL_SPACING = 15
_DEFAULT_EXPECTED_WRAPPED_Y = 30.0
_TWO_OBJECTS = 2
_FOUR_OBJECTS = 4
_DEFAULT_GRID_OBJECT_COUNT = 3


def test_place_check_args_rejects_invalid_inputs(capsys: CaptureFixture[str]) -> None:
    """Reject malformed placement argument combinations."""
    patch = MaxPatch(verbose=False)

    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button",),
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="grid",
            spacing="bad",
            starting_pos=None,
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button", "toggle"),
            randpick=True,
            num_objs=1,
            seed=None,
            weights=[1.0],
            spacing_type="grid",
            spacing=[1, 1],
            starting_pos=None,
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button",),
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="diagonal",
            spacing=[1, 1],
            starting_pos=None,
        )

    num_objs, starting_pos = patch.place_check_args(
        ("button", "toggle"),
        randpick=True,
        num_objs=[3],
        seed=None,
        weights=[0.5, 0.5],
        spacing_type="random",
        spacing=[1, 1],
        starting_pos="bad",
    )
    assert num_objs == _DEFAULT_RANDOM_OBJECT_COUNT
    assert starting_pos is None
    assert "starting position must be [x, y]" in capsys.readouterr().out


def test_place_check_args_handles_seeded_random_warning(
    capsys: CaptureFixture[str],
) -> None:
    """Report seeded random limitation when a list of counts is provided."""
    patch = MaxPatch(verbose=False)
    num_objs, _ = patch.place_check_args(
        ("button", "toggle"),
        randpick=True,
        num_objs=[3],
        seed=_DEFAULT_RANDOM_SEED,
        weights=[0.5, 0.5],
        spacing_type="random",
        spacing=[1, 1],
        starting_pos=None,
    )
    assert num_objs == _DEFAULT_RANDOM_OBJECT_COUNT
    assert (
        "warning: randpick only uses the first element of num_objs to determine "
        "the number of objects picked" in capsys.readouterr().out
    )


def test_place_pick_objs_expands_and_randomly_selects() -> None:
    """Verify deterministic and random object selection behavior."""
    patch = MaxPatch(verbose=False)
    assert patch.place_pick_objs(
        ["toggle", "button"],
        randpick=False,
        num_objs=[1, 2],
        seed=None,
        weights=None,
        verbose=False,
    ) == [
        "toggle",
        "button",
        "button",
    ]

    picks = patch.place_pick_objs(
        ["toggle", "button"],
        randpick=True,
        num_objs=4,
        seed=3,
        weights=[0.5, 0.5],
        verbose=False,
    )
    assert len(picks) == _FOUR_OBJECTS
    assert set(picks).issubset({"toggle", "button"})

    random_without_seed = patch.place_pick_objs(
        ["button", "toggle"],
        randpick=True,
        num_objs=2,
        seed=None,
        weights=[0.5, 0.5],
        verbose=False,
    )
    assert len(random_without_seed) == _TWO_OBJECTS


def test_place_check_args_supports_defaults_and_rejects_more_modes() -> None:
    """Verify defaults and invalid mode combinations raise assertions."""
    patch = MaxPatch(verbose=False)

    assert patch.place_check_args(
        ("toggle",),
        randpick=False,
        num_objs=None,
        seed=None,
        weights=None,
        spacing_type="grid",
        spacing=_KNOWN_GRID_DEFAULT,
        starting_pos=[1, 2],
    ) == (1, [1, 2])
    assert (
        patch.place_check_args(
            ("toggle",),
            randpick=True,
            num_objs=None,
            seed=None,
            weights=None,
            spacing_type="random",
            spacing=[10, 20],
            starting_pos=None,
        )[0]
        == 1
    )

    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",),
            randpick=False,
            num_objs=[1, 2],
            seed=None,
            weights=None,
            spacing_type="grid",
            spacing=[10, 20],
            starting_pos=None,
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",),
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="vertical",
            spacing=[10, 20],
            starting_pos=None,
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",),
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="bogus",
            spacing=[10, 20],
            starting_pos=None,
        )


def test_place_validators_raise_on_bad_types_and_options() -> None:
    """The high-level place entrypoint guards bools, ints, and unknown keywords."""
    patch = MaxPatch(verbose=False)

    with pytest.raises(TypeError, match="randpick must be a bool"):
        patch.place("toggle", randpick="bad")
    with pytest.raises(TypeError, match="seed must be an int or None"):
        patch.place("toggle", seed="bad")
    with pytest.raises(TypeError, match="unexpected keyword arguments: bogus"):
        patch.place("toggle", bogus=True)


def test_place_check_args_rejects_too_many_legacy_positional_flags() -> None:
    """Legacy positional mapping enforces its count limit."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        TypeError,
        match="too many positional arguments for place_check_args",
    ):
        patch.place_check_args(
            ("toggle",),
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="grid",
            spacing=[1, 1],
            starting_pos=None,
        )


def test_place_check_args_rejects_invalid_object_specs() -> None:
    """Object normalization enforces allowed spec types."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        AssertionError,
        match="objs list must be strings or existing MaxObjects",
    ):
        patch.place_check_args(
            (123,),
            randpick=False,
            num_objs=1,
            seed=None,
            weights=None,
            spacing_type="grid",
            spacing=[1, 1],
            starting_pos=None,
        )


def test_place_check_args_random_weights_length_mismatch() -> None:
    """Mismatched weight lengths raise before placement."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        AssertionError,
        match="length of weights must match length of objs",
    ):
        patch.place_check_args(
            ("toggle", "button"),
            randpick=True,
            num_objs=2,
            seed=None,
            weights=[0.5],
            spacing_type="grid",
            spacing=[1, 1],
            starting_pos=None,
        )


def test_place_check_args_rejects_incorrect_repeated_counts() -> None:
    """Repeated count lists must match the objects list length."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        AssertionError,
        match="length of num_objs must match length of objs",
    ):
        patch.place_check_args(
            ("toggle", "button"),
            randpick=False,
            num_objs=[1],
            seed=None,
            weights=None,
            spacing_type="grid",
            spacing=[1, 1],
            starting_pos=None,
        )


def test_place_check_args_custom_spacing_rejects_invalid_counts() -> None:
    """Custom spacing enforces numeric num_objs even when random."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        AssertionError,
        match="randpick custom spacing requires a numeric num_objs value",
    ):
        patch.place_check_args(
            ("toggle", "button"),
            randpick=True,
            num_objs="bad",
            seed=None,
            weights=None,
            spacing_type="custom",
            spacing=[[1, 1], [2, 2]],
            starting_pos=None,
        )

    with pytest.raises(
        AssertionError,
        match="custom spacing requires a numeric num_objs value",
    ):
        patch.place_check_args(
            ("toggle", "button"),
            randpick=False,
            num_objs="bad",
            seed=None,
            weights=None,
            spacing_type="custom",
            spacing=[[1, 1], [2, 2]],
            starting_pos=None,
        )

    with pytest.raises(
        AssertionError,
        match=(
            "spacing_type=custom: must give one position for each object in objs list"
        ),
    ):
        patch.place_check_args(
            ("toggle", "button"),
            randpick=False,
            num_objs=[1, 1],
            seed=None,
            weights=None,
            spacing_type="custom",
            spacing=[[1, 1]],
            starting_pos=None,
        )


def test_place_pick_objs_error_paths() -> None:
    """Random and deterministic pickers guard input normalizations."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(
        AssertionError,
        match="randpick requires a numeric num_objs value",
    ):
        patch.place_pick_objs(
            ["toggle"],
            randpick=True,
            num_objs="bad",
            seed=None,
            weights=None,
            verbose=False,
        )
    with pytest.raises(
        AssertionError,
        match="non-random placement requires num_objs to be normalized first",
    ):
        patch.place_pick_objs(
            ["toggle"],
            randpick=False,
            num_objs=None,
            seed=None,
            weights=None,
            verbose=False,
        )


def test_place_check_args_supports_custom_spacing_modes() -> None:
    """Verify random and non-random custom spacing modes accept expected shapes."""
    patch = MaxPatch(verbose=False)

    custom_counts, custom_positions = patch.place_check_args(
        ("button", "toggle"),
        randpick=False,
        num_objs=[1, 2],
        seed=None,
        weights=None,
        spacing_type="custom",
        spacing=[[1, 1], [2, 2], [3, 3]],
        starting_pos=None,
    )
    assert custom_counts == [1, 2]
    assert custom_positions is None


def test_place_check_args_random_custom_counts() -> None:
    """Random custom spacing counts respect the number of picks."""
    patch = MaxPatch(verbose=False)
    rand_custom_counts, _ = patch.place_check_args(
        ("button", "toggle"),
        randpick=True,
        num_objs=2,
        seed=None,
        weights=[0.5, 0.5],
        spacing_type="custom",
        spacing=[[1, 1], [2, 2]],
        starting_pos=None,
    )
    assert rand_custom_counts == _TWO_OBJECTS


def test_placing_module_helpers_raise_type_errors() -> None:
    """Direct module calls exercise helper-backed type and legacy validation."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(TypeError, match="randpick must be a bool"):
        placing_module.place(patch, "toggle", randpick="bad")
    with pytest.raises(TypeError, match="seed must be an int or None"):
        placing_module.place(patch, "toggle", seed="bad")
    with pytest.raises(TypeError, match="unexpected keyword arguments: extra"):
        placing_module.place(patch, "toggle", extra=True)
    with pytest.raises(
        TypeError,
        match="too many positional arguments for place_check_args",
    ):
        placing_module.place_check_args(
            patch,
            ("toggle",),
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
        )


def test_place_main_layout_methods() -> None:
    """Verify all placement styles return expected objects and coordinates."""
    patch = MaxPatch(verbose=False)

    grid = patch.place(
        "button",
        "toggle",
        num_objs=[1, 2],
        spacing_type="grid",
        spacing=[10, 10],
        verbose=False,
    )
    assert len(grid) == _DEFAULT_GRID_OBJECT_COUNT

    custom = patch.place(
        "number", spacing_type="custom", spacing=[[1, 2]], verbose=False
    )
    assert custom[0].raw_dict["box"]["patching_rect"][:2] == [1, 2]

    vertical = patch.place(
        "message",
        spacing_type="vertical",
        spacing=_CUSTOM_VERTICAL_SPACING,
        verbose=False,
    )
    assert vertical[0].raw_dict["box"]["patching_rect"][1] == patch.curr_position[1]

    random = patch.place(
        "toggle", randpick=True, seed=1, spacing_type="random", verbose=False
    )
    assert random[0].name == "toggle"

    random_weighted = patch.place(
        "toggle",
        "button",
        randpick=True,
        num_objs=[_TWO_OBJECTS],
        seed=1,
        weights=[0.5, 0.5],
        spacing_type="random",
        verbose=False,
    )
    assert len(random_weighted) == _TWO_OBJECTS

    seeded_in_place = patch.place(
        "toggle",
        randpick=True,
        num_objs=1,
        seed=None,
        spacing_type="random",
        verbose=False,
    )[0]
    assert seeded_in_place.name == "toggle"


def test_place_wraps_when_canvas_is_small() -> None:
    """Verify object placement wraps when canvas width is constrained."""
    patch = MaxPatch(verbose=False)
    patch.__dict__["_patcher_dict"]["patcher"]["rect"][2] = _DEFAULT_CANVAS_WIDTH
    patch.place_grid(["button", "toggle"], [10, 10], verbose=False)
    assert patch.curr_position == [10.0, _DEFAULT_EXPECTED_WRAPPED_Y]


def test_place_obj_and_get_obj_from_spec() -> None:
    """Verify object placement returns objects and spec lookup is stable."""
    patch = MaxPatch(verbose=False)
    placed = patch.place_obj("toggle", position=[1.0, 2.0], verbose=False)
    assert placed.raw_dict["box"]["id"] == "obj-1"
    assert placed.raw_dict["box"]["patching_rect"][:2] == [1.0, 2.0]
    assert placed.name == "toggle"

    assert patch.get_obj_from_spec("number").name == "number"
    assert patch.get_obj_from_spec(MaxObject("button")).name == "button"

    with pytest.raises(AssertionError):
        patch.get_obj_from_spec(object())

    with pytest.warns(UnknownObjectWarning, match="Unknown Max object"):
        unknown = patch.place("not-a-real-object", verbose=True)
    assert unknown[0].notknown() is True
