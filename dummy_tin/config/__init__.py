import copy

from . import v0
from . import v1

from .v1 import *

currentversion = v1._version

# chain of update path
_update_chain = [v1._update]

def solve_version(d):
    """ solve version difference,
    argument map d is deepcopied.
    """
    # make copy
    d = copy.deepcopy(d)
    v = d.get('version', 0)

    # functions in _update
    for f in _update_chain[v:]:
        d = f(d)

    return d
