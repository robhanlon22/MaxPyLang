"""Placement helpers used by :class:`maxpylang.maxpatch.MaxPatch`."""

from __future__ import annotations

import logging
import secrets
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Union, cast

import numpy as np

from maxpylang.maxobject import MaxObject

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

ObjectSpec = Union[str, MaxObject, list[Any]]
ObjectSequence = Sequence[ObjectSpec]
CountValue = Union[int, float]
CountSpec = Union[CountValue, list[CountValue], None]
Position = Union[list[float], tuple[float, float]]
Positions = list[Position]

_POSITION_SIZE = 2
_LEGACY_PLACE_CHECK_ARGS = (
    "randpick",
    "num_objs",
    "seed",
    "weights",
    "spacing_type",
    "spacing",
    "starting_pos",
)
_LEGACY_PLACE_PICK_ARGS = ("randpick", "num_objs", "seed", "weights", "verbose")
_LEGACY_PLACE_OBJECT_ARGS = ("verbose", "replace_id")
_DEFAULT_SPACING: Position = [80.0, 80.0]
_DEFAULT_POSITION: Position = [0.0, 0.0]
_LOGGER = logging.getLogger(__name__)


def _assertion_error(message: str) -> AssertionError:
    """Build an `AssertionError` instance."""
    return AssertionError(message)


def _type_error(message: str) -> TypeError:
    """Build a `TypeError` instance."""
    return TypeError(message)


def _bool_option(
    options: dict[str, object],
    name: str,
    *,
    default: bool,
) -> bool:
    """Pop a boolean option with a default."""
    value = options.pop(name, default)
    if isinstance(value, bool):
        return value
    message = f"{name} must be a bool"
    raise _type_error(message)


def _optional_int_option(
    options: dict[str, object],
    name: str,
) -> int | None:
    """Pop an optional integer option."""
    value = options.pop(name, None)
    if value is None or isinstance(value, int):
        return value
    message = f"{name} must be an int or None"
    raise _type_error(message)


def _assert_no_options(options: dict[str, object]) -> None:
    """Raise if unsupported keyword options remain."""
    if options:
        names = ", ".join(sorted(options))
        message = f"unexpected keyword arguments: {names}"
        raise _type_error(message)


def _apply_legacy_args(
    options: dict[str, object],
    args: tuple[object, ...],
    names: tuple[str, ...],
    context: str,
) -> None:
    """Map legacy positional arguments into named options."""
    if len(args) > len(names):
        message = f"too many positional arguments for {context}"
        raise _type_error(message)
    for name, value in zip(names, args):
        options.setdefault(name, value)


def _random_seed() -> int:
    """Generate a non-cryptographic placement seed without `random`."""
    return secrets.randbelow(2**32)


def _validate_objs(objs: ObjectSequence) -> None:
    """Ensure placement specs are strings, lists, or `MaxObject` instances."""
    for obj in objs:
        if isinstance(obj, (MaxObject, str, list)):
            continue
        message = "objs list must be strings or existing MaxObjects"
        raise _assertion_error(message)


def _normalize_num_objs(
    objs: ObjectSequence,
    *,
    randpick: bool,
    num_objs: CountSpec,
) -> CountSpec:
    """Normalize the `num_objs` option."""
    if num_objs is not None:
        return num_objs
    if randpick:
        return len(objs)
    return 1


def _normalize_random_counts(
    objs: ObjectSequence,
    num_objs: CountSpec,
    weights: list[float] | None,
) -> CountSpec:
    """Validate count and weight options for random picking."""
    normalized = num_objs
    if isinstance(normalized, list):
        _LOGGER.warning(
            "warning: randpick only uses the first element of num_objs to "
            "determine the number of objects picked"
        )
        normalized = int(normalized[0])
    if weights is not None and len(weights) != len(objs):
        message = "length of weights must match length of objs"
        raise _assertion_error(message)
    return normalized


def _validate_repeated_counts(objs: ObjectSequence, num_objs: CountSpec) -> None:
    """Validate multiplier counts when objects are not randomly selected."""
    if isinstance(num_objs, list) and len(num_objs) != len(objs):
        message = "if num_objs is list, length of num_objs must match length of objs"
        raise _assertion_error(message)


def _custom_spacing_count(
    objs: ObjectSequence,
    *,
    randpick: bool,
    num_objs: CountSpec,
) -> int:
    """Return the number of positions required for custom placement."""
    if randpick:
        if not isinstance(num_objs, (int, float)):
            message = "randpick custom spacing requires a numeric num_objs value"
            raise _assertion_error(message)
        return int(num_objs)

    if isinstance(num_objs, list):
        return int(sum(float(num) for num in num_objs))

    if not isinstance(num_objs, (int, float)):
        message = "custom spacing requires a numeric num_objs value"
        raise _assertion_error(message)
    return int(num_objs) * len(objs)


def _validate_spacing(
    objs: ObjectSequence,
    *,
    randpick: bool,
    num_objs: CountSpec,
    spacing_type: str,
    spacing: object,
) -> None:
    """Validate spacing options for object placement."""
    if spacing_type == "grid":
        if isinstance(spacing, (list, tuple)) and len(spacing) == _POSITION_SIZE:
            return
        message = (
            "spacing_type=grid: spacing must be 2-element list or tuple "
            "of [x, y] grid spacings"
        )
        raise _assertion_error(message)

    if spacing_type == "random":
        return

    if spacing_type == "custom":
        actual_num = _custom_spacing_count(
            objs,
            randpick=randpick,
            num_objs=num_objs,
        )
        if isinstance(spacing, list) and len(spacing) == actual_num:
            return
        message = (
            "spacing_type=custom: must give one position for each object in objs list"
        )
        raise _assertion_error(message)

    if spacing_type == "vertical":
        if isinstance(spacing, (int, float)):
            return
        message = (
            "spacing_type=vertical: spacing must be int or float for vertical spacing"
        )
        raise _assertion_error(message)

    message = (
        "spacing_type not recognized, must be one of grid, random, custom, or vertical"
    )
    raise _assertion_error(message)


def _normalize_starting_pos(starting_pos: Position | None) -> Position | None:
    """Validate the starting position or clear it with a warning."""
    if starting_pos is None:
        return None
    if isinstance(starting_pos, (list, tuple)) and len(starting_pos) == _POSITION_SIZE:
        return starting_pos
    _LOGGER.error(
        "PatchError: starting position must be [x, y] list or tuple of length 2, "
        "starting position not set"
    )
    return None


def place(self: MaxPatch, *objs: ObjectSpec, **options: object) -> list[MaxObject]:
    """Place objects into the patch using one of the supported layouts.

    Args:
        self: Patch receiving the objects.
        *objs: Object specifications to place.
        **options: Placement options such as ``randpick``, ``num_objs``,
            ``seed``, ``weights``, ``spacing_type``, ``spacing``,
            ``starting_pos``, and ``verbose``.

    Returns:
        The placed objects in creation order.
    """
    randpick = _bool_option(options, "randpick", default=False)
    num_objs = cast("CountSpec", options.pop("num_objs", 1))
    seed = _optional_int_option(options, "seed")
    weights = cast("list[float] | None", options.pop("weights", None))
    spacing_type = cast("str", options.pop("spacing_type", "grid"))
    spacing = options.pop("spacing", list(_DEFAULT_SPACING))
    starting_pos = cast("Position | None", options.pop("starting_pos", None))
    verbose = _bool_option(options, "verbose", default=False)
    _assert_no_options(options)

    num_objs, starting_pos = self.place_check_args(
        objs,
        randpick=randpick,
        num_objs=num_objs,
        seed=seed,
        weights=weights,
        spacing_type=spacing_type,
        spacing=spacing,
        starting_pos=starting_pos,
    )

    if starting_pos is not None:
        self.set_position(
            starting_pos[0],
            starting_pos[1],
            from_place=True,
            verbose=verbose,
        )

    picked_objs = self.place_pick_objs(
        objs,
        randpick=randpick,
        num_objs=num_objs,
        seed=seed,
        weights=weights,
        verbose=verbose,
    )

    if spacing_type == "grid":
        return self.place_grid(picked_objs, cast("Position", spacing), verbose=verbose)
    if spacing_type == "custom":
        return self.place_custom(
            picked_objs,
            cast("Positions", spacing),
            verbose=verbose,
        )
    if spacing_type == "vertical":
        return self.place_vertical(
            picked_objs,
            float(cast("int | float", spacing)),
            verbose=verbose,
        )

    random_seed = _random_seed() if seed is None else seed
    return self.place_random(picked_objs, random_seed, verbose=verbose)


def place_check_args(
    self: MaxPatch,
    objs: ObjectSequence,
    *args: object,
    **options: object,
) -> tuple[CountSpec, Position | None]:
    """Validate placement arguments and normalize the result.

    Args:
        self: Patch receiving the objects.
        objs: Candidate object specifications.
        *args: Legacy positional placement arguments.
        **options: Placement options mirrored from ``place``.

    Returns:
        A normalized ``(num_objs, starting_pos)`` tuple.
    """
    del self
    _apply_legacy_args(options, args, _LEGACY_PLACE_CHECK_ARGS, "place_check_args")

    randpick = _bool_option(options, "randpick", default=False)
    num_objs = cast("CountSpec", options.pop("num_objs", 1))
    _optional_int_option(options, "seed")
    weights = cast("list[float] | None", options.pop("weights", None))
    spacing_type = cast("str", options.pop("spacing_type", "grid"))
    spacing = options.pop("spacing", list(_DEFAULT_SPACING))
    starting_pos = cast("Position | None", options.pop("starting_pos", None))
    _assert_no_options(options)

    _validate_objs(objs)
    normalized_num_objs = _normalize_num_objs(
        objs,
        randpick=randpick,
        num_objs=num_objs,
    )
    if randpick:
        normalized_num_objs = _normalize_random_counts(
            objs,
            normalized_num_objs,
            weights,
        )
    else:
        _validate_repeated_counts(objs, normalized_num_objs)
    _validate_spacing(
        objs,
        randpick=randpick,
        num_objs=normalized_num_objs,
        spacing_type=spacing_type,
        spacing=spacing,
    )
    normalized_starting_pos = _normalize_starting_pos(starting_pos)
    return normalized_num_objs, normalized_starting_pos


def place_pick_objs(
    self: MaxPatch,
    objs: ObjectSequence,
    *args: object,
    **options: object,
) -> list[ObjectSpec]:
    """Expand or randomly choose the object specs to place.

    Args:
        self: Patch receiving the objects.
        objs: Candidate object specifications.
        *args: Legacy positional selection arguments.
        **options: Selection options mirrored from ``place``.

    Returns:
        A concrete list of object specs ready for layout.
    """
    del self
    _apply_legacy_args(options, args, _LEGACY_PLACE_PICK_ARGS, "place_pick_objs")

    randpick = _bool_option(options, "randpick", default=False)
    num_objs = cast("CountSpec", options.pop("num_objs", 1))
    seed = _optional_int_option(options, "seed")
    weights = cast("list[float] | None", options.pop("weights", None))
    _bool_option(options, "verbose", default=False)
    _assert_no_options(options)

    if randpick:
        random_seed = _random_seed() if seed is None else seed
        rng = np.random.default_rng(random_seed)
        _LOGGER.debug(
            "Patcher: picking %s random objects with seed %s",
            num_objs,
            random_seed,
        )
        if not isinstance(num_objs, (int, float)):
            message = "randpick requires a numeric num_objs value"
            raise _assertion_error(message)
        choices = np.array(list(objs), dtype=object)
        picked = rng.choice(choices, size=int(num_objs), p=weights)
        return list(cast("list[ObjectSpec]", picked.tolist()))

    if isinstance(num_objs, (int, float)):
        counts = [int(num_objs)] * len(objs)
    else:
        if num_objs is None:
            message = "non-random placement requires num_objs to be normalized first"
            raise _assertion_error(message)
        counts = [int(num) for num in num_objs]

    picked_objs: list[ObjectSpec] = []
    for obj, count in zip(objs, counts):
        picked_objs.extend([obj] * count)
    return picked_objs


def place_grid(
    self: MaxPatch,
    objs: ObjectSequence,
    spacing: Position,
    **options: object,
) -> list[MaxObject]:
    """Place objects on a grid derived from the patch cursor.

    Args:
        self: Patch receiving the objects.
        objs: Object specifications to place.
        spacing: Horizontal and vertical grid spacing.
        **options: Keyword options. Supported key is ``verbose``.

    Returns:
        The placed objects.
    """
    verbose = _bool_option(options, "verbose", default=False)
    _assert_no_options(options)
    _LOGGER.debug(
        "Patcher: placing %s objects with grid spacings of %s",
        len(objs),
        spacing,
    )

    x_space = float(spacing[0])
    y_space = float(spacing[1])
    curr_x = self._curr_position[0]
    curr_y = self._curr_position[1]

    if curr_y == 0:
        curr_y += y_space

    canvas_x = cast("float", self._patcher_dict["patcher"]["rect"][2])
    created_objs: list[MaxObject] = []
    for obj in objs:
        curr_x += x_space
        if curr_x > (canvas_x - x_space):
            curr_x = x_space
            curr_y += y_space
        created_objs.append(
            self.place_obj(obj, position=[curr_x, curr_y], verbose=verbose),
        )

    self._curr_position = [curr_x, curr_y]
    return created_objs


def place_random(
    self: MaxPatch,
    objs: ObjectSequence,
    seed: int,
    **options: object,
) -> list[MaxObject]:
    """Place objects at random positions on the patch canvas.

    Args:
        self: Patch receiving the objects.
        objs: Object specifications to place.
        seed: Seed for NumPy's random generator.
        **options: Keyword options. Supported key is ``verbose``.

    Returns:
        The placed objects.
    """
    verbose = _bool_option(options, "verbose", default=False)
    _assert_no_options(options)
    _LOGGER.debug("Patcher: placing %s objects randomly with seed %s", len(objs), seed)

    rng = np.random.default_rng(seed)
    width = float(self._patcher_dict["patcher"]["rect"][2])
    height = float(self._patcher_dict["patcher"]["rect"][3])

    created_objs: list[MaxObject] = []
    for obj in objs:
        position = [float(rng.random() * width), float(rng.random() * height)]
        created_objs.append(self.place_obj(obj, position=position, verbose=verbose))
    return created_objs


def place_custom(
    self: MaxPatch,
    objs: ObjectSequence,
    positions: Positions,
    **options: object,
) -> list[MaxObject]:
    """Place objects at explicit positions.

    Args:
        self: Patch receiving the objects.
        objs: Object specifications to place.
        positions: One coordinate pair per object.
        **options: Keyword options. Supported key is ``verbose``.

    Returns:
        The placed objects.
    """
    verbose = _bool_option(options, "verbose", default=False)
    _assert_no_options(options)
    _LOGGER.debug(
        "Patcher: placing %s objects with custom positions of %s",
        len(objs),
        positions,
    )

    created_objs: list[MaxObject] = []
    current_position: Position = [self._curr_position[0], self._curr_position[1]]
    for obj, current_position in zip(objs, positions):
        created_objs.append(
            self.place_obj(obj, position=current_position, verbose=verbose),
        )

    self._curr_position = list(current_position)
    return created_objs


def place_vertical(
    self: MaxPatch,
    objs: ObjectSequence,
    spacing: float,
    **options: object,
) -> list[MaxObject]:
    """Place objects vertically from the current cursor position.

    Args:
        self: Patch receiving the objects.
        objs: Object specifications to place.
        spacing: Vertical distance between successive objects.
        **options: Keyword options. Supported key is ``verbose``.

    Returns:
        The placed objects.
    """
    verbose = _bool_option(options, "verbose", default=False)
    _assert_no_options(options)
    _LOGGER.debug(
        "Patcher: placing %s objects with vertical spacing of %s",
        len(objs),
        spacing,
    )

    x_pos = self._curr_position[0] + spacing
    y_pos = self._curr_position[1]
    created_objs: list[MaxObject] = []
    for obj in objs:
        y_pos += spacing
        created_objs.append(
            self.place_obj(obj, position=[x_pos, y_pos], verbose=verbose),
        )

    self._curr_position = [x_pos, y_pos]
    return created_objs


def place_obj(
    self: MaxPatch,
    obj: ObjectSpec,
    position: Position = _DEFAULT_POSITION,
    *args: object,
    **options: object,
) -> MaxObject:
    """Place a single object into the patch.

    Args:
        self: Patch receiving the object.
        obj: Object specification to place.
        position: Target ``[x, y]`` location.
        *args: Legacy positional ``verbose`` and ``replace_id`` arguments.
        **options: Keyword options. Supported keys are ``verbose`` and
            ``replace_id``.

    Returns:
        The placed object instance.
    """
    _apply_legacy_args(options, args, _LEGACY_PLACE_OBJECT_ARGS, "place_obj")
    _bool_option(options, "verbose", default=False)
    replace_id = cast("str | None", options.pop("replace_id", None))
    _assert_no_options(options)

    placed_obj = self.get_obj_from_spec(obj)
    if replace_id is None:
        self._num_objs += 1
        placed_obj.set_box_id(f"obj-{self._num_objs}")
    else:
        placed_obj.set_box_id(replace_id)

    placed_obj.raw_dict["box"]["patching_rect"][0:2] = position
    self._objs[placed_obj.box_id] = placed_obj

    message = f"Patcher: {placed_obj.name}"
    if placed_obj.notknown():
        message += " (unknown)"
    message += f" added, total objects {self._num_objs}"
    _LOGGER.debug(message)

    return placed_obj


def get_obj_from_spec(self: MaxPatch, obj_spec: ObjectSpec) -> MaxObject:
    """Return a `MaxObject` from a placement spec."""
    del self
    if isinstance(obj_spec, str):
        return MaxObject(obj_spec)
    if isinstance(obj_spec, MaxObject):
        return obj_spec
    message = "object must be specified as a string or a MaxObject"
    raise _assertion_error(message)
