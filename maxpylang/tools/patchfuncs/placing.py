"""
tools.patchfuncs.placing

Methods related to placing objects in a MaxPatch.

    place() --> user function, driver for placing objs

    place_check_args() --> check that arguments given are correct
    place_pick_objs() --> generate list of objs to be placed (picked randomly or multiplied from given list)

    place_random() --> place objects randomly
    place_grid() --> place objects on grid
    place_custom() --> place objects with custom spacing
    place_vertical() --> place objects with vertical spacing

    place_obj() --> place a single object
    get_obj_from_spec() --> return object from specification (either MaxObject or string)

"""

from __future__ import annotations

import random
from collections.abc import Sequence
from typing import Any, List, Optional, Tuple, Union, cast

import numpy as np

from maxpylang.maxobject import MaxObject

ObjectSpec = Union[str, MaxObject, List[Any]]
ObjectSequence = Sequence[ObjectSpec]
CountSpec = Optional[Union[int, float, List[Union[int, float]]]]
Position = Union[List[float], Tuple[float, float]]


# for user usage
def place(
    self: Any,
    *objs: ObjectSpec,
    randpick: bool = False,
    num_objs: CountSpec = 1,
    seed: Optional[int] = None,
    weights: Optional[List[float]] = None,
    spacing_type: str = "grid",
    spacing: Any = [80.0, 80.0],
    starting_pos: Optional[Position] = None,
    verbose: bool = False,
) -> list[MaxObject]:
    """
    Place objects in the patch.

            objs --> list of object names as strings, OR list of objects as prev. created MaxObjects (or mix of both)
        randpick --> True: pick n random objs from objs list (default pick 1)
              - num_objs --> integer: n = num_objs
              - num_objs --> list: give error & take first element on list
              - num_objs --> None: n = len(objs)
        randpick --> False: pick all objs on objs list (default each picked once)
              - num_objs --> integer: each obj multiplied by num_objs
              - num_objs --> list: each objs multiplied by corresponding num_objs entry
              - num_objs --> None: n = len(objs)
            seed --> random seed for picking/placing objs, if None then random seed
         weights --> weight probabilities for picking objs, if None then equal probability
    spacing_type --> options for how to place objs on canvas
              - "grid": objects centered on a grid
                    - spacing --> tuple/list length 2: [x, y] grid spacings
              - "random": random locations, using same seed as before (overlaps possible)
                    - spacing --> N/A
              - "custom": location specified for each object
                    - spacing --> list: positions [[x, y]], can only be used for num_objs=1
              - "vertical": objects stacked vertically
                    - spacing --> number: specify height
    starting_pos --> starting position to place from, must be tuple/list length 2: [x, y]

    verbose --> print output for seed, etc.

    :returns: a list of the MaxObjects that have been created

    """
    # check arguments are correct
    num_objs, starting_pos = cast(
        "Tuple[CountSpec, Optional[Position]]",
        self.place_check_args(
            objs, randpick, num_objs, seed, weights, spacing_type, spacing, starting_pos
        ),
    )

    # set the starting position
    if starting_pos is not None:
        self.set_position(
            starting_pos[0], starting_pos[1], from_place=True, verbose=verbose
        )

    # generate total list of objects to be placed
    picked_objs = cast(
        "list[ObjectSpec]",
        self.place_pick_objs(objs, randpick, num_objs, seed, weights, verbose),
    )

    # place objects according to spacing
    if spacing_type == "grid":
        placed_objs = cast(
            "list[MaxObject]", self.place_grid(picked_objs, spacing, verbose=verbose)
        )
    elif spacing_type == "custom":
        placed_objs = cast(
            "list[MaxObject]", self.place_custom(picked_objs, spacing, verbose=verbose)
        )
    elif spacing_type == "random":
        if seed is None:  # generate seed if not given
            seed = random.randrange(2**32 - 1)
        placed_objs = cast(
            "list[MaxObject]", self.place_random(picked_objs, seed, verbose=verbose)
        )
    else:
        assert spacing_type == "vertical"
        placed_objs = cast(
            "list[MaxObject]",
            self.place_vertical(picked_objs, spacing, verbose=verbose),
        )

    return placed_objs


# check arguments
def place_check_args(
    self: Any,
    objs: ObjectSequence,
    randpick: bool,
    num_objs: CountSpec,
    seed: Optional[int],
    weights: Optional[List[float]],
    spacing_type: str,
    spacing: Any,
    starting_pos: Optional[Position],
) -> Tuple[CountSpec, Optional[Position]]:
    """
    Helper function for placing objects.

    Check that all arguments are formatted correctly.
    Format num_objs correctly.
    """
    # check objs
    for obj in objs:
        assert isinstance(obj, (MaxObject, str, list)), (
            "objs list must be strings or existing MaxObjects"
        )

    # check num_objs
    if num_objs is None:
        if not randpick:  # if not randomly picking, num_objs refers to how many multiples of each given object
            num_objs = 1  # default to 1
        if (
            randpick
        ):  # if randomly picking, num_objs refers to how many random selections to make
            num_objs = len(
                objs
            )  # default to randomly selecting as many objs as are given

    # check randpick possibilities
    if not randpick:
        if isinstance(
            num_objs, list
        ):  # giving number of multiples for each given object
            assert len(num_objs) == len(objs), (
                "if num_objs is list, length of num_objs must match length of objs"
            )
    elif randpick:
        if isinstance(num_objs, list):  # only take the first number for random picking
            print(
                "warning: randpick only uses the first element of num_objs to determine the number of objects picked"
            )
            num_objs = int(num_objs[0])
        if weights is not None:
            assert len(weights) == len(objs), (
                "length of weights must match length of objs"
            )

    # check spacing args
    if spacing_type == "grid":
        assert isinstance(spacing, (list, tuple)) and len(spacing) == 2, (
            "spacing_type=grid: spacing must "
            "be 2-element list or tuple of [x, y] grid spacings"
        )
    elif spacing_type == "random":
        pass
    elif spacing_type == "custom":
        # tricky num_objs dealing here....
        # case 1: randpick = False, num_objs is an integer
        # case 2: randpick = False, num_objs is a list
        # case 3: randpick = True, num_objs is an integer
        if not randpick:
            if isinstance(num_objs, list):
                # num_objs specifies a multiplier for each obj in objs_list
                actual_num = int(sum(float(num) for num in num_objs))
            else:
                assert isinstance(num_objs, (int, float))
                actual_num = int(num_objs) * len(objs)
        elif randpick:
            # num_objs is the number of objects being picked
            assert isinstance(num_objs, (int, float))
            actual_num = int(num_objs)
        assert isinstance(spacing, (list)) and len(spacing) == actual_num, (
            "spacing_type=custom: must give one position for each object in objs list"
        )
    elif spacing_type == "vertical":
        assert isinstance(spacing, (int, float)), (
            "spacing_type=vertical: spacing must be int or float for vertical spacing"
        )
    else:
        assert False, (
            "spacing_type not recognized, must be one of grid, random, custom, or vertical"
        )

    if starting_pos is not None:
        if not (isinstance(starting_pos, (list, tuple)) and len(starting_pos) == 2):
            print(
                " PatchError: starting position must be [x, y] list or tuple of length 2, starting position not set"
            )
            starting_pos = None

    return num_objs, starting_pos


# pick objects
def place_pick_objs(
    self: Any,
    objs: ObjectSequence,
    randpick: bool,
    num_objs: CountSpec,
    seed: Optional[int],
    weights: Optional[List[float]],
    verbose: bool,
) -> list[ObjectSpec]:
    """
    Helper function for placing objects.

    Returns list of picked objects to place, either picked randomly or multiplied from given list.
    """
    del self
    picked_objs: list[ObjectSpec] = []

    # picking randomly
    if randpick:
        if seed is None:  # generate seed if not given
            seed = random.randrange(2**32 - 1)
        np.random.seed(seed)  # set seed
        if verbose:
            print("Patcher: picking", num_objs, "random objects with seed", seed)
        assert isinstance(num_objs, (int, float))
        choices = np.array(list(objs), dtype=object)
        picked_objs = list(np.random.choice(choices, size=int(num_objs), p=weights))

    # multiply from given list
    elif not randpick:
        if isinstance(num_objs, (int, float)):  # make num_objs into proper list form
            counts = [int(num_objs)] * len(objs)
        else:
            assert num_objs is not None
            counts = [int(num) for num in num_objs]

        for obj, num in zip(
            objs, counts
        ):  # make copies of each obj, according to num_obj
            picked_objs += [obj] * num

    return picked_objs


# spacing
def place_grid(
    self: Any, objs: ObjectSequence, spacing: Position, verbose: bool = False
) -> list[MaxObject]:
    """
    Helper function for placing.
    Places objects in a grid.
    """
    if verbose:
        print("Patcher: placing", len(objs), "objects with grid spacings of", spacing)

    x_space = float(spacing[0])
    y_space = float(spacing[1])

    # get current positions
    curr_x = self._curr_position[0]
    curr_y = self._curr_position[1]

    # if current y pos is 0, go down one row so we're not starting at the very top of the page
    if curr_y == 0:
        curr_y += y_space

    canvas_x = self._patcher_dict["patcher"]["rect"][2]

    created_objs: list[MaxObject] = []

    for obj in objs:
        curr_x += x_space
        if curr_x > (canvas_x - x_space):
            curr_x = x_space
            curr_y += y_space
        placed_obj = self.place_obj(obj, position=[curr_x, curr_y], verbose=verbose)
        created_objs.append(placed_obj)

    self._curr_position = [curr_x, curr_y]

    return created_objs


# spacing
def place_random(
    self: Any, objs: ObjectSequence, seed: int, verbose: bool = False
) -> list[MaxObject]:
    """
    Helper function for placing.
    Places objects randomly.
    """
    if verbose:
        print("Patcher: placing", len(objs), "objects randomly with seed", seed)  # log

    np.random.seed(seed)  # set seed

    # get canvas size
    x = self._patcher_dict["patcher"]["rect"][2]
    y = self._patcher_dict["patcher"]["rect"][3]

    created_objs: list[MaxObject] = []
    for obj in objs:
        position = [np.random.random() * x, np.random.random() * y]
        placed_obj = self.place_obj(obj, position=position, verbose=verbose)
        created_objs.append(placed_obj)

    return created_objs


# spacing
def place_custom(
    self: Any, objs: ObjectSequence, positions: List[Position], verbose: bool = False
) -> list[MaxObject]:
    """
    Helper function for placing.
    Places objects according to custom positions.
    """
    if verbose:
        print(
            "Patcher: placing", len(objs), "objects with custom positions of", positions
        )  # log

    created_objs: list[MaxObject] = []
    pos: Position = [self._curr_position[0], self._curr_position[1]]
    for obj, pos in zip(objs, positions):
        placed_obj = self.place_obj(obj, position=pos, verbose=verbose)
        created_objs.append(placed_obj)

    self._curr_position = pos

    return created_objs


# spacing
def place_vertical(
    self: Any, objs: ObjectSequence, spacing: float, verbose: bool = False
) -> list[MaxObject]:
    """
    Helper function for placing.
    Places objects vertically.
    """
    if verbose:
        print(
            "Patcher: placing", len(objs), "objects with vertical spacing of", spacing
        )

    x = self._curr_position[0] + spacing
    y = self._curr_position[1]

    created_objs: list[MaxObject] = []
    for obj in objs:
        y += spacing
        placed_obj = self.place_obj(obj, position=[x, y], verbose=verbose)
        created_objs.append(placed_obj)

    self._curr_position = [x, y]

    return created_objs


# actual placement of a single object
def place_obj(
    self: Any,
    obj: ObjectSpec,
    position: Position = (0.0, 0.0),
    verbose: bool = False,
    replace_id: Optional[str] = None,
) -> MaxObject:
    """
    Helper function for placing.
    If obj denoted by string, creates obj; otherwise, adds existing object to patcher at specified position.

    obj --> object to be placed (str or MaxObject)
    position --> patcher position
    verbose --> debug commands
    replace_id --> 'obj-num' string of object being replaced
    """
    obj = cast("MaxObject", self.get_obj_from_spec(obj))

    if replace_id is None:  # for just adding (not replacing)...
        self._num_objs += 1  # increment patch number of objects
        obj._dict["box"]["id"] = "obj-" + str(
            self._num_objs
        )  # change obj id to number of patch objects
    else:
        obj._dict["box"]["id"] = replace_id  # change obj id to replacement id

    obj._dict["box"]["patching_rect"][0:2] = position  # change position

    # add to various dictionaries of patch objects by obj-id
    obj_id = cast("str", obj._dict["box"]["id"])
    self._objs[obj_id] = obj

    if verbose:
        print("Patcher:", obj.name, end="")
        if obj.notknown():
            print(" (unknown)", end="")
        print(" added, total objects", self._num_objs)  # log

    return obj


# also used in replace
def get_obj_from_spec(self: Any, obj_spec: ObjectSpec) -> MaxObject:
    """
    Helper function to get object from specification, either from string or from MaxObject.
    """
    # if given as string, make object (warning fires from MaxObject constructor)
    if isinstance(obj_spec, str):
        obj: MaxObject = MaxObject(obj_spec)

    # otherwise, make sure it's a MaxObject
    else:
        assert isinstance(obj_spec, MaxObject), (
            "object must be specified as a string or a MaxObject"
        )
        obj = obj_spec

    return obj
