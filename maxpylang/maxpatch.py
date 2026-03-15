"""
Class representing a MaxPatch.
"""

from __future__ import annotations

import os
from typing import Any, cast

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


class MaxPatch:
    """
    This class represents a MaxMSP patch. A MaxPatch can be created as a copy of a template file,
    or by loading in an existing *.maxpat* file.

    :param template: the path to a template *.maxpat* file. Can be given as an absolute path, a relative path
                     from the current directory, or a relative path from ``MaxPy/maxpy/data/PATCH_TEMPLATES/``.
    :type template: str, optional; default: None

    :param load_file: the path to an existing *.maxpat* file to be loaded in.
                      Can be given as an absolute path or a relative path from the current directory.
    :type load_file: str, optional; default: None

    :param reorder: whether or not to reassign object ids after loading in an existing file. See :func:`MaxPatch.reorder`.
    :type reorder: bool, optional; default: True

    :param verbose: for logging output.
    :type verbose: bool, optional; default: True
    """

    patch_templates_path = _constants.patch_templates_path

    def __init__(
        self,
        template: str | None = None,
        load_file: str | None = None,
        reorder: bool = True,
        verbose: bool = True,
    ) -> None:
        """
        Constructor method.
        """
        self._objs: ObjectDict = {}
        self._num_objs = 0
        self._patcher_dict: JSONDict = {}
        self._curr_position: list[float] = [0.0, 0.0]
        self._filename = "default.maxpat"

        if load_file:
            self.load_file(load_file, reorder=reorder, verbose=verbose)
        else:
            if template is None:
                template = os.path.join(
                    self.patch_templates_path, "empty_template.json"
                )
            self.load_template(template, verbose=verbose)

    @property
    def objs(self) -> ObjectDict:
        """
        A dictionary of all Max objects in the patch, stored by object id. Read-only.
        """
        return self._objs

    @property
    def num_objs(self) -> int:
        """
        The number of Max objects in the patch. Read-only.
        """
        return self._num_objs

    @property
    def curr_position(self) -> list[float]:
        """
        The current position of the 'cursor' at which to place Max objects. Given as a two-element list [x, y] of patch coordinates.
        Can be set using :func:`MaxPatch.set_position`.
        """
        return self._curr_position

    @property
    def dict(self) -> JSONDict:
        """
        The JSON dict of the patch. Read-only.
        """
        return self.get_json()

    def load_template(self, t: str, verbose: bool = True) -> None:
        _instantiation.load_template(self, t, verbose=verbose)

    def load_file(self, f: str, reorder: bool = True, verbose: bool = True) -> None:
        _instantiation.load_file(self, f, reorder=reorder, verbose=verbose)

    def load_objs_from_dict(self, patch_dict: JSONDict, verbose: bool = True) -> None:
        _instantiation.load_objs_from_dict(self, patch_dict, verbose=verbose)

    def load_patchcords_from_dict(
        self, patch_dict: JSONDict, verbose: bool = True
    ) -> None:
        _instantiation.load_patchcords_from_dict(self, patch_dict, verbose=verbose)

    def clean_patcher_dict(self, patch_dict: JSONDict) -> JSONDict:
        return _instantiation.clean_patcher_dict(self, patch_dict)

    def reorder(self, verbose: bool = False) -> None:
        _exposed.reorder(self, verbose=verbose)

    def set_position(
        self,
        new_x: float,
        new_y: float,
        from_place: bool = False,
        verbose: bool = False,
    ) -> None:
        _exposed.set_position(
            self, new_x, new_y, from_place=from_place, verbose=verbose
        )

    def replace(
        self,
        curr_obj_num: str,
        new_obj: Any,
        retain: bool = True,
        verbose: bool = False,
        **new_attribs: Any,
    ) -> None:
        _exposed.replace(
            self,
            curr_obj_num,
            new_obj,
            retain=retain,
            verbose=verbose,
            **new_attribs,
        )

    def inspect(self, *objs: str, info: str = "all") -> None:
        _exposed.inspect(self, *objs, info=info)

    def save(
        self, filename: str = "default.maxpat", verbose: bool = True, check: bool = True
    ) -> None:
        _saving.save(self, filename=filename, verbose=verbose, check=check)

    def get_json(self) -> JSONDict:
        return _saving.get_json(self)

    def place(
        self,
        *objs: _placing.ObjectSpec,
        randpick: bool = False,
        num_objs: _placing.CountSpec = 1,
        seed: int | None = None,
        weights: list[float] | None = None,
        spacing_type: str = "grid",
        spacing: Any = None,
        starting_pos: _placing.Position | None = None,
        verbose: bool = False,
    ) -> list[MaxObject]:
        if spacing is None:
            spacing = [80.0, 80.0]
        return _placing.place(
            self,
            *objs,
            randpick=randpick,
            num_objs=num_objs,
            seed=seed,
            weights=weights,
            spacing_type=spacing_type,
            spacing=spacing,
            starting_pos=starting_pos,
            verbose=verbose,
        )

    def place_check_args(
        self,
        objs: Any,
        randpick: bool,
        num_objs: _placing.CountSpec,
        seed: int | None,
        weights: Any,
        spacing_type: str,
        spacing: Any,
        starting_pos: Any,
    ) -> tuple[_placing.CountSpec, Any]:
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
        objs: Any,
        randpick: bool,
        num_objs: _placing.CountSpec,
        seed: int | None,
        weights: Any,
        verbose: bool,
    ) -> list[_placing.ObjectSpec]:
        return _placing.place_pick_objs(
            self, objs, randpick, num_objs, seed, weights, verbose
        )

    def place_grid(
        self, objs: Any, spacing: Any, verbose: bool = False
    ) -> list[MaxObject]:
        return _placing.place_grid(self, objs, spacing, verbose=verbose)

    def place_random(
        self, objs: Any, seed: int, verbose: bool = False
    ) -> list[MaxObject]:
        return _placing.place_random(self, objs, seed, verbose=verbose)

    def place_custom(
        self,
        objs: Any,
        positions: Any,
        verbose: bool = False,
    ) -> list[MaxObject]:
        return _placing.place_custom(self, objs, positions, verbose=verbose)

    def place_vertical(
        self, objs: Any, spacing: float, verbose: bool = False
    ) -> list[MaxObject]:
        return _placing.place_vertical(self, objs, spacing, verbose=verbose)

    def place_obj(
        self,
        obj: _placing.ObjectSpec,
        position: _placing.Position | None = None,
        verbose: bool = False,
        replace_id: str | None = None,
    ) -> MaxObject:
        if position is None:
            position = [0.0, 0.0]
        return _placing.place_obj(
            self, obj, position=position, verbose=verbose, replace_id=replace_id
        )

    def get_obj_from_spec(self, obj_spec: _placing.ObjectSpec) -> MaxObject:
        return _placing.get_obj_from_spec(self, obj_spec)

    def connect(self, *connections: ConnectionSpec, verbose: bool = True) -> None:
        _patchcords.connect(self, *connections, verbose=verbose)

    def swap_patchcords(self, new: MaxObject, old: MaxObject) -> None:
        _patchcords.swap_patchcords(self, new, old)

    def check_connection_format(self, connections: Any) -> None:
        _patchcords.check_connection_format(self, connections)

    def check_connection_typing(self, connections: Any) -> Any:
        return _patchcords.check_connection_typing(self, connections)

    def check_connection_exists(self, connections: Any) -> list[ConnectionSpec]:
        return _patchcords.check_connection_exists(self, connections)

    def delete(
        self,
        objs: Any = None,
        cords: Any = None,
        verbose: bool = True,
    ) -> None:
        _deleting.delete(self, objs=objs, cords=cords, verbose=verbose)

    def delete_get_extra_cords(self, *objs: str) -> list[ConnectionSpec]:
        return _deleting.delete_get_extra_cords(self, *objs)

    def delete_cords(self, *cords: ConnectionSpec, verbose: bool = True) -> None:
        _deleting.delete_cords(self, *cords, verbose=verbose)

    def delete_objs(self, *objs: str, verbose: bool = True) -> None:
        _deleting.delete_objs(self, *objs, verbose=verbose)

    def check(self, *flags: str) -> None:
        _checking.check(self, *flags)

    def get_unknowns(self) -> ObjectDict:
        return cast("ObjectDict", _checking.get_unknowns(self))

    def get_abstractions(self) -> ObjectDict:
        return cast("ObjectDict", _checking.get_abstractions(self))

    def get_js_objs(self) -> tuple[ObjectDict, ObjectDict]:
        return cast("tuple[ObjectDict, ObjectDict]", _checking.get_js_objs(self))

    def add_barebones_obj(self, obj_text: str) -> None:
        _misc.add_barebones_obj(self, obj_text)
