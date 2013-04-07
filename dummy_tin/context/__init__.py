import copy

import v0
import v1

from v1 import *

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

if __name__ == '__main__':
    defs = [v0.default, v1.default]
    exs = [v0.example, v1.example]
    
    print 'test default'
    for i, d in enumerate(defs):
        upd = solve_version(d)
        print i
        assert(upd==defs[currentversion])

    print 'test example'
    for i, d in enumerate(exs):
        upd = solve_version(d)
        print i
        assert(upd==exs[currentversion])
