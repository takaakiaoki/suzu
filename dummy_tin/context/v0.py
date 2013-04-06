_version = 0

proj_default = {'symbol':'H', 'z':1, 'w':1.008, 'energy':10, 'angle':0}

proj_example = {'symbol':'Si', 'z':14, 'w':29.977, 'energy':1000, 'angle':45}

layer_default = [{
        'name':'Layer',
        'width': 100000,
        'wunit': 'Ang',
        'dens': 0.0,
        'corr': 1.0,
        'gas': False,
        'atomtbl':[]
        }]

layer_example = [
        {'name':'Silicon', 'width':100, 'wunit':'Ang', 'dens':2.3212,
            'corr':1.0, 'gas':False,
            'atomtbl':[
                {'symbol':'Si', 'z':14, 'w':28.088,
                    'stoich':1, 'disp':[15, 2, 4.7]}]},
        {'name':'Water', 'width':1, 'wunit':'um', 'dens':0.00125,
            'corr':0.94, 'gas':True,
            'atomtbl':[
                {'symbol':'H', 'z':1, 'w':1.008, 'stoich':2,
                    'disp':[10, 3, 2]},
                {'symbol':'O', 'z':8, 'w':15.999, 'stoich':1,
                    'disp':[28, 3, 2]}]}
        ]

param1_default = {
            'calcname':'',
            'autosave':10000,
            'totalion':99999,
            'randseed':0,
            'windowmin':0,
            'windowmax':0}

param1_example = {
            'calcname':'suzu test',
            'autosave':100,
            'totalion':1,
            'randseed':117,
            'windowmin':100,
            'windowmax':1000}

param2_default = {
        'ionrange':False,
        'bscatter':False,
        'transmit':0,
        'sputter':False,
        'collidetail':0,
        'einterval':0}

param2_example = {
        'ionrange':True,
        'bscatter':True,
        'transmit':1,
        'sputter':True,
        'collidetail':1,
        'einterval':25}

root_default = {
        'damage':1,
        'plots':0,
        'proj':proj_default,
        'layer':layer_default,
        'param1':param1_default,
        'param2':param2_default
}

root_example = {
        'damage':2,
        'plots':4,
        'proj':proj_example,
        'layer':layer_example,
        'param1':param1_example,
        'param2':param2_example
}

default = root_default
example = root_example
