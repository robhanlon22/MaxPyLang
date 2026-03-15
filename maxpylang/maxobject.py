"""
Class representing a MaxObject.
"""

from __future__ import annotations

from typing import Any, Optional

from .tools import constants as _constants
from .tools import misc
from .tools.objfuncs import args as _args
from .tools.objfuncs import attribs as _attribs
from .tools.objfuncs import exposed as _exposed
from .tools.objfuncs import instantiation as _instantiation
from .tools.objfuncs import makexlets as _makexlets
from .tools.objfuncs import misc as _obj_misc
from .tools.objfuncs import reffile as _reffile
from .tools.objfuncs import specialobjs as _specialobjs
from .tools.objfuncs import text as _text
from .xlet import Inlet, Outlet


class MaxObject:
    """
    This class represents a Max object within a Max patch.

    To create a *cycle~* object with a frequency of 440 Hz, you would use the in-box text: ``"cycle~ 440"``.

    You can also include attributes in the in-box text by using the '@' symbol followed by the attribute name and value.
    For example, to create a *jit.movie* object that loads the file *crashtest.mov*, you would use the in-box text:
    ``"jit.movie @moviefile crashtest.mov"``.
    TODO: this seems to not work for UI objects maybe.

    Objects have inlets and outlets, which are accessible via the ``.ins`` and ``.outs`` properties, respectively.
    You can access individual inlets and outlets by indexing into these lists. For example, to access the first outlet of an object
    named *myobj*, you would use ``myobj.outs[0]``.
    """

    arg_warning = True
    known_objs = misc.get_objs()
    common_box_attribs = _constants.common_box_attribs
    obj_info_folder = _constants.obj_info_folder
    unknown_obj_dict = _constants.unknown_obj_dict

    def __init__(
        self,
        text: Any,
        from_dict: bool = False,
        abstraction: bool = False,
        inlets: int | None = None,
        outlets: int | None = None,
        **extra_attribs: Any,
    ) -> None:
        """
        Initialize a MaxObject.

        from_dict = False --> initialize from in-box text (normal initialization in Max env)
            text --> in-box text
            extra_attribs --> attributes to change, formatted as attribute_name = val

        from_dict = True --> initialize from given json dict representation of obj (for loading in from existing file)
            text --> json dict
            extra_attribs --> not used
        abstraction = True --> treat as abstraction without needing the .maxpat file in cwd
            inlets --> number of inlets (default 0)
            outlets --> number of outlets (default 0)
        """
        self._ref_file: Optional[str] = None
        self._dict: dict[str, Any] = {}
        self._name: str = ""
        self._args: list[Any] = []
        self._text_attribs: dict[str, Any] = {}
        self._ins: list[Inlet] = []
        self._outs: list[Outlet] = []
        self._ext_file: Optional[str] = None

        if from_dict:
            self.build_from_dict(text)
        else:
            self.build_from_specs(
                text,
                extra_attribs,
                abstraction=abstraction,
                inlets=inlets,
                outlets=outlets,
            )

    @property
    def name(self) -> str:
        """
        The name of the MaxObject, e.g. 'sel', 'bang', 'js'.
        """
        return self._name

    @property
    def ins(self) -> list[Inlet]:
        """
        A list of Inlet objects attached to the MaxObject.
        """
        return self._ins

    @property
    def outs(self) -> list[Outlet]:
        """
        A list of Outlet objects attached to the MaxObject.
        """
        return self._outs

    def move(self, x: float, y: float) -> None:
        _exposed.move(self, x, y)

    def edit(
        self, text_add: str = "append", text: Optional[str] = None, **extra_attribs: Any
    ) -> None:
        _exposed.edit(self, text_add=text_add, text=text, **extra_attribs)

    def link(self, link_file: Optional[str] = None) -> None:
        _exposed.link(self, link_file=link_file)

    def inspect(self) -> None:
        _exposed.inspect(self)

    def build_from_specs(
        self,
        text: str,
        extra_attribs: dict[str, Any],
        abstraction: bool = False,
        inlets: int | None = None,
        outlets: int | None = None,
    ) -> None:
        _instantiation.build_from_specs(
            self,
            text,
            extra_attribs,
            abstraction=abstraction,
            inlets=inlets,
            outlets=outlets,
        )

    def build_from_dict(self, given_dict: dict[str, Any]) -> None:
        _instantiation.build_from_dict(self, given_dict)

    def parse_text(self, text: str) -> tuple[str, list[Any], dict[str, Any]]:
        return _text.parse_text(self, text)

    def update_text(self) -> None:
        _text.update_text(self)

    def get_text(self) -> str:
        return _text.get_text(self)

    def get_ref(self, name: str) -> str:
        return _reffile.get_ref(self, name)

    def check_aliases(self, name: str) -> str:
        return _reffile.check_aliases(self, name)

    def get_info(self, ref_file: Optional[str] = None) -> dict[str, Any]:
        return _reffile.get_info(self, ref_file=ref_file)

    def make_xlets_from_self_dict(self) -> None:
        _makexlets.make_xlets_from_self_dict(self)

    def update_ins_outs(
        self, inout_info: dict[str, Any], default_info: dict[str, Any]
    ) -> None:
        _makexlets.update_ins_outs(self, inout_info, default_info)

    def parse_io_num(self, info: list[dict[str, Any]], default_num: int) -> int:
        return _makexlets.parse_io_num(self, info, default_num)

    def add_xlets(self, num: int, xlet_type: str) -> None:
        _makexlets.add_xlets(self, num, xlet_type)

    def remove_xlets(self, num: int, xlet_type: str) -> None:
        _makexlets.remove_xlets(self, num, xlet_type)

    def update_dict_io_nums(self) -> None:
        _makexlets.update_dict_io_nums(self)

    def update_xlet_typing(
        self, info: dict[str, Any], xlet_type: str, num_xlets: int
    ) -> None:
        _makexlets.update_xlet_typing(self, info, xlet_type, num_xlets)

    def parse_io_typing(self, type_info: Any, num_xlets: int) -> list[Any]:
        return _makexlets.parse_io_typing(self, type_info, num_xlets)

    def args_valid(self, name: str, args: list[Any], arg_info: dict[str, Any]) -> bool:
        return _args.args_valid(self, name, args, arg_info)

    def get_typed_args(self, args: list[str]) -> list[Any]:
        return _args.get_typed_args(self, args)

    def add_extra_attribs(self, extra_attribs: dict[str, Any]) -> None:
        _attribs.add_extra_attribs(self, extra_attribs)

    def get_all_valid_attribs(
        self,
        text_attribs: dict[str, Any],
        extra_attribs: dict[str, Any],
        attrib_info: list[dict[str, Any]],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        return _attribs.get_all_valid_attribs(
            self, text_attribs, extra_attribs, attrib_info
        )

    def remove_bad_attribs(
        self, attribs: dict[str, Any], attrib_speclist: list[dict[str, Any]]
    ) -> dict[str, Any]:
        return _attribs.remove_bad_attribs(self, attribs, attrib_speclist)

    def retain_attribs(self, other: MaxObject) -> None:
        _attribs.retain_attribs(self, other)

    def get_extra_attribs(self) -> dict[str, Any]:
        return _attribs.get_extra_attribs(self)

    def create_js(self, from_dict: Optional[bool] = None) -> None:
        _specialobjs.create_js(self, from_dict=from_dict)

    def get_js_filename(self) -> Optional[str]:
        return _specialobjs.get_js_filename(self)

    def get_js_io(
        self, filename: str, log_var: Optional[str] = None
    ) -> tuple[Any, Any]:
        return _specialobjs.get_js_io(self, filename, log_var=log_var)

    def update_js_from_file(self, filename: str, log_var: Optional[str] = None) -> None:
        _specialobjs.update_js_from_file(self, filename, log_var=log_var)

    def link_js(self, link_file: Optional[str] = None) -> None:
        _specialobjs.link_js(self, link_file=link_file)

    def create_abstraction(
        self,
        text: Optional[str] = None,
        extra_attribs: Optional[dict[str, Any]] = None,
        from_dict: bool = True,
    ) -> None:
        _specialobjs.create_abstraction(
            self, text=text, extra_attribs=extra_attribs, from_dict=from_dict
        )

    def get_abstraction_io(self) -> tuple[int, int]:
        return _specialobjs.get_abstraction_io(self)

    def update_abstraction_from_file(
        self,
        text: str,
        extra_attribs: Optional[dict[str, Any]],
        log_var: Optional[str] = None,
    ) -> None:
        _specialobjs.update_abstraction_from_file(
            self, text, extra_attribs, log_var=log_var
        )

    def link_abstraction(self, link_file: Optional[str] = None) -> None:
        _specialobjs.link_abstraction(self, link_file=link_file)

    def create_declared_abstraction(
        self,
        text: str,
        numinlets: int,
        numoutlets: int,
        extra_attribs: dict[str, Any],
    ) -> None:
        _specialobjs.create_declared_abstraction(
            self, text, numinlets, numoutlets, extra_attribs
        )

    def get_trigger_out_types(self) -> list[str]:
        return _specialobjs.get_trigger_out_types(self)

    def get_unpack_out_types(self) -> list[str]:
        return _specialobjs.get_unpack_out_types(self)

    def update_vst(self) -> None:
        _specialobjs.update_vst(self)

    def notknown(self) -> bool:
        return _obj_misc.notknown(self)

    def __repr__(self) -> str:
        return _obj_misc.__repr__(self)

    def debug(self) -> None:
        print("ref_file", self._ref_file)
        print("dict", self._dict)
        print("name", self._name)
        print("args", self._args)
        print("text_attribs", self._text_attribs)
        print("ins", self._ins)
        print("outs", self._outs)
        print("ext_file", self._ext_file)
