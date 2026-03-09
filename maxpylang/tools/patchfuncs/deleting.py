"""
tools.patchfuncs.deleting

Methods related to deleting objects and patchcords from a MaxPatch.

    delete() --> driver method for deleting objs/patchcords

    delete_get_extra_cords() --> get a list of all patchcords attached to objs being deleted
    delete_cords() --> delete patchcords
    delete_objs() --> delete objects

"""

from typing import Any, Optional, Sequence


Connection = list[Any]


# delete objects and patchcords
def delete(
    self: Any,
    objs: Optional[Sequence[str]] = None,
    cords: Optional[Sequence[Connection]] = None,
    verbose: bool = True,
) -> None:
    """
    Delete objects and/or patchcords.
    Deleting objects will automatically delete any patchcords attached to them.

     objs --> list of string "obj-num" objects to delete
    cords --> list of connections (Outlet, Inlet)
    """

    obj_ids = list(objs or [])
    cord_list = list(cords or [])

    # check format
    for obj in obj_ids:
        assert isinstance(obj, str), (
            "objects to delete must be given as strings 'obj-num'"
        )
    self.check_connection_format(cord_list)

    # remove nonexistent cords
    cord_list = self.check_connection_exists(cord_list)

    # delete cords
    self.delete_cords(*cord_list, verbose=verbose)

    # delete objs
    self.delete_objs(*obj_ids, verbose=verbose)

    return


def delete_get_extra_cords(self: Any, *objs: str) -> list[Connection]:
    """
    Helper function for deleting.

    Gets patchcords attached to objects being deleted and adds to cords list.
    Returns updated cords list.
    """

    cords: list[Connection] = []
    for obj_id in objs:
        if obj_id in self._objs.keys():
            obj = self._objs[obj_id]
            # add cords coming from object to list for deletion
            for outlet in obj.outs:
                for dest_inlet in outlet.destinations:
                    cords.append([outlet, dest_inlet])
            # add cords coming to object to list for deletion
            for inlet in obj.ins:
                for source_outlet in inlet.sources:
                    cords.append([source_outlet, inlet])

    # just to be sure...
    self.check_connection_format(cords)  # check proper formatting of cords

    return cords


def delete_cords(self: Any, *cords: Connection, verbose: bool = True) -> None:
    """
    Helper function for deleting.

    Delete cords in list.
    Cords must be specified as (Outlet, Inlet) pairs
    """

    for cord in cords:
        outlet = cord[0]
        inlet = cord[1]
        midpoints = inlet._midpoints[inlet.sources.index(outlet)]

        # delete inlet from outlet destinations
        outlet._destinations.remove(inlet)
        # delete outlet from inlet sources
        inlet._sources.remove(outlet)
        # delete corresponding midpoint from inlet midpoints
        inlet._midpoints.remove(midpoints)

        if verbose:
            print(
                "disconnected: (",
                outlet.parent.name,
                ": outlet",
                outlet.index,
                "-/->",
                inlet.parent.name,
                ": inlet",
                inlet.index,
                ")",
            )

    return


def delete_objs(self: Any, *objs: str, verbose: bool = True) -> None:
    """
    Helper function for deleting.

    Deletes objects on list.
    Also deletes any patchcords attached to those objects.

    Objects must be specified as 'obj-num' strings
    """

    obj_ids = list(objs)

    # check for obj existence
    for obj in obj_ids.copy():
        if obj not in self.objs.keys():  # if object in patch
            print(
                "delete error:", obj, "not in patch"
            )  # if obj not in patch, print error
            obj_ids.remove(obj)  # and remove from delete list

    # get patchcords connected to objs, for deletion
    cords_to_delete = self.delete_get_extra_cords(*obj_ids)
    # delete patchcords
    self.delete_cords(*cords_to_delete)

    # delete objects
    for obj in obj_ids:
        obj_name = self._objs[obj].name  # save for logging
        del self._objs[obj]

        if verbose:
            print("object deleted:", obj, obj_name)

    self._num_objs = len(self._objs)

    return
