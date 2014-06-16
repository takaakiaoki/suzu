import copy

_version = 1

default = {
        'version':_version,
        'lastdir':'',
        'srimcompoundpath':''
        }

def _update(d):
    """update from v0 to v1"""
    newd = copy.deepcopy(default)

    if 'lastdir' in d:
        newd['lastdir'] = d['lastdir']

    return newd
