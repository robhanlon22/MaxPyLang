"""Public facade for building, editing, and serializing Max patchers."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

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

JSONDict = dict[str, Any]
ObjectDict = dict[str, MaxObject]
ConnectionSpec = list[Any]
ConnectionCollection = list[ConnectionSpec]
_MAX_LEGACY_FLAGS = 2

if TYPE_CHECKING:
    from collections.abc import Sequence


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
    """Represent a Max patcher and the objects it contains.

    Instances keep track of placed objects, patchcords, and the current
    placement cursor. Most public methods are thin convenience wrappers around
    the implementation modules under ``maxpylang.tools.patchfuncs`` so callers
    can work with a single, stable facade.
    """

    patch_templates_path = _constants.patch_templates_path

    def __init__(
        self,
        template: str | None = None,
        load_file: str | None = None,
        *args: object,
        **options: object,
    ) -> None:
        """Initialize a patch from a template or an existing file.

        Args:
            template: Path to a template JSON file. When omitted and
                ``load_file`` is not provided, the bundled empty template is
                used.
            load_file: Existing ``.maxpat`` file to load instead of starting
                from a template.
            *args: Legacy positional flags mapped to ``reorder`` and
                ``verbose`` for backwards compatibility.
            **options: Keyword options. Supported keys are ``reorder`` and
                ``verbose``.

        Raises:
            TypeError: If too many legacy positional flags are supplied or a
                supported option has the wrong type.
        """
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
        """Load patcher state from a template JSON file.

        Args:
            template: Path to the template file to load.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.

        Raises:
            TypeError: If an unsupported option is supplied or a flag has the
                wrong type.
        """
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
        """Load patch data from an existing ``.maxpat`` file.

        Args:
            filename: Path to the patch file on disk.
            *args: Legacy positional flags mapped to ``reorder`` and
                ``verbose``.
            **options: Keyword options. Supported keys are ``reorder`` and
                ``verbose``.

        Raises:
            TypeError: If too many legacy flags are supplied or a supported
                option has the wrong type.
        """
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
        """Serialize the patch to disk.

        Args:
            filename: Output path. ``.maxpat`` is appended automatically when
                needed.
            *args: Legacy positional flags mapped to ``verbose`` and ``check``.
            **options: Keyword options. Supported keys are ``verbose`` and
                ``check``.

        Raises:
            TypeError: If too many legacy flags are supplied or a supported
                option has the wrong type.
        """
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
        """Return the current patch as a Max-compatible dictionary.

        Returns:
            The serialized patcher structure, including object boxes and
            patchcord lines.
        """
        return _saving.get_json(self)

    def place(self, *objs: _placing.ObjectSpec, **options: object) -> list[MaxObject]:
        """Create one or more objects and place them in the patch.

        Args:
            *objs: Object specifications. Each item can be an object text
                string, an existing ``MaxObject``, or a compatible legacy list
                spec.
            **options: Placement controls such as ``randpick``, ``num_objs``,
                ``seed``, ``weights``, ``spacing_type``, ``spacing``,
                ``starting_pos``, and ``verbose``.

        Returns:
            The newly placed ``MaxObject`` instances in placement order.

        Raises:
            AssertionError: If placement arguments are structurally invalid.
            TypeError: If option types are invalid or unsupported options are
                supplied.
        """
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
        objs: _placing.ObjectSequence,
        *args: object,
        **options: object,
    ) -> tuple[_placing.CountSpec, _placing.Position | None]:
        """Normalize and validate placement options without placing objects.

        Args:
            objs: Object specifications that would be passed to ``place``.
            *args: Legacy positional placement arguments.
            **options: Placement options mirrored from ``place``.

        Returns:
            A tuple of ``(num_objs, starting_pos)`` after normalization.

        Raises:
            AssertionError: If the placement combination is not valid.
            TypeError: If option types are invalid or unexpected options are
                supplied.
        """
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
            objs,
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
        objs: _placing.ObjectSequence,
        *args: object,
        **options: object,
    ) -> list[_placing.ObjectSpec]:
        """Expand repeated object specs or randomly pick from them.

        Args:
            objs: Candidate object specifications.
            *args: Legacy positional selection arguments.
            **options: Selection options mirrored from ``place``.

        Returns:
            A concrete list of object specifications ready for placement.

        Raises:
            AssertionError: If the selection arguments are internally
                inconsistent.
            TypeError: If option types are invalid or unexpected options are
                supplied.
        """
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
            objs,
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
        """Place objects on a grid using the current cursor as an origin.

        Args:
            objs: Object specifications to place.
            spacing: Horizontal and vertical grid spacing.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.

        Returns:
            The newly placed objects.
        """
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
        """Place objects at random positions on the patch canvas.

        Args:
            objs: Object specifications to place.
            seed: Seed used to generate deterministic random coordinates.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.

        Returns:
            The newly placed objects.
        """
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
        """Place objects at explicit coordinates.

        Args:
            objs: Object specifications to place.
            positions: One ``[x, y]`` pair per object.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.

        Returns:
            The newly placed objects.
        """
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
        """Place objects vertically from the current cursor position.

        Args:
            objs: Object specifications to place.
            spacing: Vertical distance between successive objects.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.

        Returns:
            The newly placed objects.
        """
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
        """Place a single object into the patch.

        Args:
            obj: Object specification to place.
            position: Target ``[x, y]`` position. When omitted, ``[0.0, 0.0]``
                is used.
            *args: Legacy positional flags mapped to ``verbose`` and
                ``replace_id``.
            **options: Keyword options. Supported keys are ``verbose`` and
                ``replace_id``.

        Returns:
            The placed object instance.

        Raises:
            TypeError: If too many legacy flags are supplied or an option has
                the wrong type.
        """
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
        """Normalize a placement specification into a ``MaxObject``.

        Args:
            obj_spec: String, ``MaxObject``, or compatible legacy object spec.

        Returns:
            A ``MaxObject`` instance ready for placement.
        """
        return _placing.get_obj_from_spec(self, obj_spec)

    def connect(
        self,
        *connections: ConnectionSpec,
        **options: object,
    ) -> None:
        """Connect outlets to inlets.

        Args:
            *connections: Connection triplets or pairs in
                ``[Outlet, Inlet, midpoints?]`` form.
            **options: Keyword options. Supported key is ``verbose``.
        """
        verbose = _bool_option(options, "verbose", default=True)
        _assert_no_options(options)
        _patchcords.connect(self, *connections, verbose=verbose)

    def swap_patchcords(self, new: MaxObject, old: MaxObject) -> None:
        """Swap retained patchcords during replacement."""
        _patchcords.swap_patchcords(self, new, old)

    def check_connection_format(
        self,
        connections: tuple[ConnectionSpec, ...] | list[ConnectionSpec],
    ) -> None:
        """Validate patchcord connection formatting."""
        _patchcords.check_connection_format(self, connections)

    def check_connection_typing(
        self,
        connections: tuple[ConnectionSpec, ...] | list[ConnectionSpec],
    ) -> list[ConnectionSpec]:
        """Filter patchcords by type compatibility."""
        return _patchcords.check_connection_typing(self, connections)

    def check_connection_exists(
        self,
        connections: tuple[ConnectionSpec, ...] | list[ConnectionSpec],
    ) -> list[ConnectionSpec]:
        """Filter patchcords to those that currently exist."""
        return _patchcords.check_connection_exists(self, connections)

    def delete(
        self,
        objs: Sequence[str] | None = None,
        cords: Sequence[ConnectionSpec] | None = None,
        *args: object,
        **options: object,
    ) -> None:
        """Delete objects and/or patchcords from the patch.

        Args:
            objs: Object ids to remove.
            cords: Patchcord specs to remove.
            *args: Optional legacy positional ``verbose`` flag.
            **options: Keyword options. Supported key is ``verbose``.
        """
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
        """Run patch-level validation helpers.

        Args:
            *flags: Validation categories such as ``unknown``, ``js``,
                ``abstractions``, or ``all``.
        """
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
