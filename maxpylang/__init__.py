from .tools import constants
from .maxobject import MaxObject
from .maxpatch import MaxPatch
from .importobjs import import_objs
from .xlet import Inlet, Outlet

try:
    from . import objects
except ImportError:
    pass  # objects not yet generated
