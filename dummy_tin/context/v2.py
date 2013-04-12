import copy

import v1

_version = 2

proj_default = v1.proj_default
proj_example = v1.proj_example

atomtbl_elem_default = v1.atomtbl_elem_default
atomtbl_elem_example = v1.atomtbl_elem_example

atomtbl_default = v1.atomtbl_default
atomtbl_example = v1.atomtbl_example

layer_elem_default = v1.layer_elem_default
layer_elem_example = v1.layer_elem_example

target_default = v1.layer_default
target_example = v1.layer_example

param1_default = v1.param1_default
param1_example = v1.param1_example

param2_default = v1.param2_default
param2_example = v1.param2_example

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
        'target':target_default,
        'param1':param1_default,
        'param2':param2_default
}

root_example = {
        'version': _version,
        'model':model_example,
        'proj':proj_example,
        'target':target_example,
        'param1':param1_example,
        'param2':param2_example
}

default = root_default
example = root_example

def _update(d):
    """update from v1 to v2"""
    newd = copy.deepcopy(default)
    if 'layer' in d:
        newd['target'] = d['layer']

    for k in ('model', 'proj', 'param1', 'param2'):
        if k in d:
            newd[k] = d[k]

    return newd

if __name__ == '__main__':
    # test update
    print 'test default'
    updef = _update(v1.default)
    assert(default == updef)

    print 'test example'
    upex = _update(v1.example)
    assert(example == upex)
