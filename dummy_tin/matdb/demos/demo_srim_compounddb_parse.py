import sys
import os

__dir__ = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(__dir__, '../../..'))

import dummy_tin.matdb.srim_compounddb as compounddb


if __name__ == '__main__':
    import sys

    #cat = parse(sys.stdin)
    # load Compound.dat assumed as cp437 (for MS Linedraw fontset)
    cat = compounddb.parse(open(os.path.join(__dir__, '../Compound.dat'), 'rt', encoding='cp437'))

    for c in cat:
        print('!!!!!')
        #print(c.desc)
        print(c.get_title())

        for t in c.tables:
            print('****')
            print(t.desc)
            print(t.name)
            print(t.density)
            print(t.mass_percentage)
            print(t.elems)
            print(t.bonding)
            print(t.comment)
            print(t.fulltext)
