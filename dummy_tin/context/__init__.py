import copy

from . import v0
from . import v1
from . import v2

from .v2 import *

currentversion = v2._version

# chain of update path
_update_chain = [v1._update, v2._update]

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

if __name__ == '__main__':
    defs = [v0.default, v1.default, v2.default]
    exs = [v0.example, v1.example, v2.example]
    
    print('test default')
    for i, d in enumerate(defs):
        upd = solve_version(d)
        print(i)
        assert(upd==defs[currentversion])

    print('test example')
    for i, d in enumerate(exs):
        upd = solve_version(d)
        print(i)
        assert(upd==exs[currentversion])
