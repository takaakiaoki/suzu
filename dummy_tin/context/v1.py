import copy

import v0

_version = 1

proj_default = v0.proj_default
proj_example = v0.proj_example

atomtbl_elem_default = v0.atomtbl_elem_default
atomtbl_elem_example = v0.atomtbl_elem_example

atomtbl_default = v0.atomtbl_default
atomtbl_example = v0.atomtbl_example

layer_elem_default = v0.layer_elem_default
layer_elem_example = v0.layer_elem_example

layer_default = v0.layer_default
layer_example = v0.layer_example

param1_default = v0.param1_default
param1_example = v0.param1_example

param2_default = v0.param2_default
param2_example = v0.param2_example

model_default = {
        'damage':1,
        'plots':0,
        }

model_example = {
        'damage':2,
        'plots':4,
        }

root_default = {
        'version': _version,
        'model':model_default,
        'proj':proj_default,
        'layer':layer_default,
        'param1':param1_default,
        'param2':param2_default
}

root_example = {
        'version': _version,
        'model':model_example,
        'proj':proj_example,
        'layer':layer_example,
        'param1':param1_example,
        'param2':param2_example
}

default = root_default
example = root_example

def _update(d):
    """update from v0 to v1"""
    newd = copy.deepcopy(default)
    if 'damage' in d:
        newd['model']['damage'] = d['damage']
    if 'plots' in d:
        newd['model']['plots'] = d['plots']

    for k in ('proj', 'layer', 'param1', 'param2'):
        if k in d:
            newd[k] = d[k]

    return newd

if __name__ == '__main__':
    # test update
    print 'test default'
    updef = update(v0.default)
    assert(default == updef)

    print 'test example'
    upex = update(v0.example)
    assert(example == upex)
