"""Expose the `MaxPatch` facade."""

from __future__ import annotations

from pathlib import Path
from typing import cast

from .maxobject import MaxObject
from .tools import constants as _constants
from .tools.patchfuncs import checking as _checking
from .tools.patchfuncs import deleting as _deleting
from .tools.patchfuncs import exposed as _exposed
from .tools.patchfuncs import instantiation as _instantiation
from .tools.patchfuncs import misc as _misc
from .tools.patchfuncs import patchcords as _patchcords
from .tools.patchfuncs import placing as _placing
from .tools.patchfuncs import saving as _saving

JSONDict = dict[str, object]
ObjectDict = dict[str, MaxObject]
ConnectionSpec = list[object]
ConnectionCollection = list[ConnectionSpec]
_MAX_LEGACY_FLAGS = 2


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


class MaxPatch:
    """Represent a Max patcher."""

    patch_templates_path = _constants.patch_templates_path

    def __init__(
        self,
        template: str | None = None,
        load_file: str | None = None,
        *args: object,
        **options: object,
    ) -> None:
        """Initialize a patch from a template or an existing file."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "MaxPatch accepts at most two legacy positional flags"
            raise _type_error(message)

        if args:
            options.setdefault("reorder", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("verbose", args[1])

        reorder = _bool_option(options, "reorder", default=True)
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)

        self._objs: ObjectDict = {}
        self._num_objs = 0
        self._patcher_dict: JSONDict = {}
        self._curr_position: list[float] = [0.0, 0.0]
        self._filename = "default.maxpat"

        if load_file:
            self.load_file(load_file, reorder=reorder, verbose=verbose)
            return

        template_path = template
        if template_path is None:
            template_path = str(Path(self.patch_templates_path) / "empty_template.json")
        self.load_template(template_path, verbose=verbose)

    @property
    def objs(self) -> ObjectDict:
        """Return the patch objects keyed by box id."""
        return self._objs

    @property
    def num_objs(self) -> int:
        """Return the number of objects currently in the patch."""
        return self._num_objs

    @property
    def curr_position(self) -> list[float]:
        """Return the current placement cursor position."""
        return self._curr_position

    @property
    def dict(self) -> JSONDict:
        """Return the serialized patch dictionary."""
        return self.get_json()

    def load_template(
        self,
        template: str,
        *args: object,
        **options: object,
    ) -> None:
        """Load a patch from a template file."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _instantiation.load_template(self, template, verbose=verbose)

    def load_file(
        self,
        filename: str,
        *args: object,
        **options: object,
    ) -> None:
        """Load a patch from an existing `.maxpat` file."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "load_file accepts at most two legacy positional flags"
            raise _type_error(message)
        if args:
            options.setdefault("reorder", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("verbose", args[1])

        reorder = _bool_option(options, "reorder", default=True)
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _instantiation.load_file(self, filename, reorder=reorder, verbose=verbose)

    def load_objs_from_dict(
        self,
        patch_dict: JSONDict,
        *args: object,
        **options: object,
    ) -> None:
        """Load box objects from a serialized patch dictionary."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _instantiation.load_objs_from_dict(self, patch_dict, verbose=verbose)

    def load_patchcords_from_dict(
        self,
        patch_dict: JSONDict,
        *args: object,
        **options: object,
    ) -> None:
        """Load patchcords from a serialized patch dictionary."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _instantiation.load_patchcords_from_dict(self, patch_dict, verbose=verbose)

    def clean_patcher_dict(self, patch_dict: JSONDict) -> JSONDict:
        """Remove object and patchcord entries from a patch dictionary."""
        return _instantiation.clean_patcher_dict(self, patch_dict)

    def reorder(self, *args: object, **options: object) -> None:
        """Renumber patch objects sequentially."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        _exposed.reorder(self, verbose=verbose)

    def set_position(
        self,
        new_x: float,
        new_y: float,
        *args: object,
        **options: object,
    ) -> None:
        """Set the placement cursor position."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "set_position accepts at most two legacy positional flags"
            raise _type_error(message)
        if args:
            options.setdefault("from_place", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("verbose", args[1])

        from_place = _bool_option(options, "from_place", default=False)
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        _exposed.set_position(
            self,
            new_x,
            new_y,
            from_place=from_place,
            verbose=verbose,
        )

    def replace(
        self,
        curr_obj_num: str,
        new_obj: object,
        *args: object,
        **options: object,
    ) -> None:
        """Replace an object while preserving compatible state."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "replace accepts at most two legacy positional flags"
            raise _type_error(message)
        if args:
            options.setdefault("retain", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("verbose", args[1])

        retain = _bool_option(options, "retain", default=True)
        verbose = _bool_option(options, "verbose", default=False)
        new_attribs = dict(options)
        _exposed.replace(
            self,
            curr_obj_num,
            new_obj,
            retain=retain,
            verbose=verbose,
            **new_attribs,
        )

    def inspect(self, *objs: str, info: str = "all") -> None:
        """Inspect the patch or selected objects."""
        _exposed.inspect(self, *objs, info=info)

    def save(
        self,
        filename: str = "default.maxpat",
        *args: object,
        **options: object,
    ) -> None:
        """Serialize the patch to disk."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "save accepts at most two legacy positional flags"
            raise _type_error(message)
        if args:
            options.setdefault("verbose", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("check", args[1])

        verbose = _bool_option(options, "verbose", default=True)
        check = _bool_option(options, "check", default=True)
        _assert_no_options(options)
        _saving.save(self, filename=filename, verbose=verbose, check=check)

    def get_json(self) -> JSONDict:
        """Return the serialized patch dictionary."""
        return _saving.get_json(self)

    def place(self, *objs: _placing.ObjectSpec, **options: object) -> list[MaxObject]:
        """Place objects in the patch."""
        randpick = _bool_option(options, "randpick", default=False)
        num_objs = options.pop("num_objs", 1)
        seed = _optional_int_option(options, "seed")
        weights = options.pop("weights", None)
        spacing_type = options.pop("spacing_type", "grid")
        spacing = options.pop("spacing", [80.0, 80.0])
        starting_pos = options.pop("starting_pos", None)
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place(
            self,
            *objs,
            randpick=randpick,
            num_objs=cast("_placing.CountSpec", num_objs),
            seed=seed,
            weights=cast("list[float] | None", weights),
            spacing_type=cast("str", spacing_type),
            spacing=spacing,
            starting_pos=cast("_placing.Position | None", starting_pos),
            verbose=verbose,
        )

    def place_check_args(
        self,
        objs: object,
        *args: object,
        **options: object,
    ) -> tuple[_placing.CountSpec, _placing.Position | None]:
        """Validate placement options before object creation."""
        legacy_names = (
            "randpick",
            "num_objs",
            "seed",
            "weights",
            "spacing_type",
            "spacing",
            "starting_pos",
        )
        if len(args) > len(legacy_names):
            message = "too many positional arguments for place_check_args"
            raise _type_error(message)
        for name, value in zip(legacy_names, args):
            options.setdefault(name, value)

        randpick = _bool_option(options, "randpick", default=False)
        num_objs = cast("_placing.CountSpec", options.pop("num_objs", 1))
        seed = _optional_int_option(options, "seed")
        weights = cast("list[float] | None", options.pop("weights", None))
        spacing_type = cast("str", options.pop("spacing_type", "grid"))
        spacing = options.pop("spacing", [80.0, 80.0])
        starting_pos = cast(
            "_placing.Position | None",
            options.pop("starting_pos", None),
        )
        _assert_no_options(options)
        return _placing.place_check_args(
            self,
            cast("_placing.ObjectSequence", objs),
            randpick,
            num_objs,
            seed,
            weights,
            spacing_type,
            spacing,
            starting_pos,
        )

    def place_pick_objs(
        self,
        objs: object,
        *args: object,
        **options: object,
    ) -> list[_placing.ObjectSpec]:
        """Expand or randomly choose the objects to place."""
        legacy_names = ("randpick", "num_objs", "seed", "weights", "verbose")
        if len(args) > len(legacy_names):
            message = "too many positional arguments for place_pick_objs"
            raise _type_error(message)
        for name, value in zip(legacy_names, args):
            options.setdefault(name, value)

        randpick = _bool_option(options, "randpick", default=False)
        num_objs = cast("_placing.CountSpec", options.pop("num_objs", 1))
        seed = _optional_int_option(options, "seed")
        weights = cast("list[float] | None", options.pop("weights", None))
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place_pick_objs(
            self,
            cast("_placing.ObjectSequence", objs),
            randpick,
            num_objs,
            seed,
            weights,
            verbose,
        )

    def place_grid(
        self,
        objs: _placing.ObjectSequence,
        spacing: _placing.Position,
        *args: object,
        **options: object,
    ) -> list[MaxObject]:
        """Place objects on the patcher grid."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place_grid(self, objs, spacing, verbose=verbose)

    def place_random(
        self,
        objs: _placing.ObjectSequence,
        seed: int,
        *args: object,
        **options: object,
    ) -> list[MaxObject]:
        """Place objects at random positions on the patcher canvas."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place_random(self, objs, seed, verbose=verbose)

    def place_custom(
        self,
        objs: _placing.ObjectSequence,
        positions: object,
        *args: object,
        **options: object,
    ) -> list[MaxObject]:
        """Place objects at explicit positions."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place_custom(
            self,
            objs,
            cast("list[_placing.Position]", positions),
            verbose=verbose,
        )

    def place_vertical(
        self,
        objs: _placing.ObjectSequence,
        spacing: float,
        *args: object,
        **options: object,
    ) -> list[MaxObject]:
        """Place objects vertically."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=False)
        _assert_no_options(options)
        return _placing.place_vertical(self, objs, spacing, verbose=verbose)

    def place_obj(
        self,
        obj: _placing.ObjectSpec,
        position: _placing.Position | None = None,
        *args: object,
        **options: object,
    ) -> MaxObject:
        """Place one object into the patch."""
        if len(args) > _MAX_LEGACY_FLAGS:
            message = "place_obj accepts at most two legacy positional options"
            raise _type_error(message)
        if args:
            options.setdefault("verbose", args[0])
        if len(args) == _MAX_LEGACY_FLAGS:
            options.setdefault("replace_id", args[1])

        verbose = _bool_option(options, "verbose", default=False)
        replace_id = options.pop("replace_id", None)
        _assert_no_options(options)
        actual_position = [0.0, 0.0] if position is None else position
        return _placing.place_obj(
            self,
            obj,
            position=actual_position,
            verbose=verbose,
            replace_id=cast("str | None", replace_id),
        )

    def get_obj_from_spec(self, obj_spec: _placing.ObjectSpec) -> MaxObject:
        """Return a `MaxObject` from a placement spec."""
        return _placing.get_obj_from_spec(self, obj_spec)

    def connect(
        self,
        *connections: ConnectionSpec,
        **options: object,
    ) -> None:
        """Connect outlets to inlets."""
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _patchcords.connect(self, *connections, verbose=verbose)

    def swap_patchcords(self, new: MaxObject, old: MaxObject) -> None:
        """Swap retained patchcords during replacement."""
        _patchcords.swap_patchcords(self, new, old)

    def check_connection_format(self, connections: object) -> None:
        """Validate patchcord connection formatting."""
        _patchcords.check_connection_format(self, connections)

    def check_connection_typing(self, connections: object) -> object:
        """Filter patchcords by type compatibility."""
        return _patchcords.check_connection_typing(self, connections)

    def check_connection_exists(self, connections: object) -> list[ConnectionSpec]:
        """Filter patchcords to those that currently exist."""
        return _patchcords.check_connection_exists(self, connections)

    def delete(
        self,
        objs: object = None,
        cords: object = None,
        *args: object,
        **options: object,
    ) -> None:
        """Delete objects and/or patchcords."""
        if args:
            options.setdefault("verbose", args[0])
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _deleting.delete(self, objs=objs, cords=cords, verbose=verbose)

    def delete_get_extra_cords(self, *objs: str) -> list[ConnectionSpec]:
        """Return extra patchcords affected by object deletion."""
        return _deleting.delete_get_extra_cords(self, *objs)

    def delete_cords(self, *cords: ConnectionSpec, **options: object) -> None:
        """Delete patchcords."""
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _deleting.delete_cords(self, *cords, verbose=verbose)

    def delete_objs(self, *objs: str, **options: object) -> None:
        """Delete objects."""
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _deleting.delete_objs(self, *objs, verbose=verbose)

    def check(self, *flags: str) -> None:
        """Run patch-level validation helpers."""
        _checking.check(self, *flags)

    def get_unknowns(self) -> ObjectDict:
        """Return unresolved objects in the patch."""
        return cast("ObjectDict", _checking.get_unknowns(self))

    def get_abstractions(self) -> ObjectDict:
        """Return abstraction objects in the patch."""
        return cast("ObjectDict", _checking.get_abstractions(self))

    def get_js_objs(self) -> tuple[ObjectDict, ObjectDict]:
        """Return linked and unlinked js objects."""
        return cast("tuple[ObjectDict, ObjectDict]", _checking.get_js_objs(self))

    def add_barebones_obj(self, obj_text: str) -> None:
        """Insert a minimal object dictionary into the patch."""
        _misc.add_barebones_obj(self, obj_text)
