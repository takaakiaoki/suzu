# translate srim compound database to suzu layer_element

import dummy_tin.physics.element as element
import dummy_tin.db.disp as displacement
import compounddb

def srim_to_suzu(c):
    """
    c: parsed object of srim compound data
    """

    # if ratio is given as mass percentage, transrate it
    table = []
    for z, r in c.elems:
        sym = element.table_bynum[z].sym
        w = element.table_bynum[z].mass
        if c.mass_percentage:
            r /= w
        table.append({
            'symbol':sym,
            'z':z,
            'w':w,
            'stoich':r,
            'disp':displacement.disp[sym]})

    layer = {
        'name': c.name,
        'dens': c.density,
        'atomtbl':table}

    return layer
