""" parse SRIM compound data base
"""

import cStringIO
import re

class Compound(object):
    def __init__(self):
        self.desc = '' # target description
        self.name = '' # name of table
        self.mass_percentage = False # F: atom%, T:
        self.density = 0.0 #density
        self.elems = []  # (atomnum, atom%)
        self.bonding = [0.0] * 18 
        self.comment = ''

def parse(input):
    """parse into tables
    """
    ST_UNDEFINED = 0
    ST_CAT_DESC = 1
    ST_TBL_DATA = 2

    state = ST_UNDEFINED

    tables = []

    buf = ''
    for line in input.readlines():
        if line[0] == '!':
            if state == ST_TBL_DATA:
                # close buffer and parse the contentents
                toparse = cStringIO.StringIO(buf)
                # pass to the parser..
                tables.append(parse_target_table(toparse))

                # clear buffer
                buf = ''
            state = ST_CAT_DESC

        elif line[0] == '*':
            if state == ST_TBL_DATA:
                # close buffer and parse the contentents
                toparse = cStringIO.StringIO(buf)
                # pass to the parser..
                tables.append(parse_target_table(toparse))

                # enter new target entry
                buf = line
            else:
                # enter new target entry
                buf = line
            state = ST_TBL_DATA

        else: # other line
            if state == ST_TBL_DATA:
                buf += line

    return tables

def parse_target_table(input):
    t = Compound()
    # 1st line, description, remove heading '*'
    t.desc = input.readline()[1:]

    # 2nd line, name, density, elements
    t.name, t.mass_percentage, t.dens, t.elems = parse_target_data(input.readline())

    # 3rd line, bonding 
    t.bonding = [float(d) for d in input.readline().split()]

    # last comment (begin with '$')
    for line in input.readlines():
        if line[0] == '$':
            t.comment += line[1:]
        else:
            t.comment += line

    return t

seperator = re.compile(r'\s*,*\s*')

def parse_target_data(s):
    # "name", dens, elems, elem1 no, elem1 ratio, ...
    # parse "name", and following
    v = s.split('"')
    # v[0] == '', v[2]== ', 0.00125, 2, 1, 2, 8, 1'
    name = v[1]
    # test atom_mass persentage
    mass_percentage = (name[0] == '%')
    #if needed, truncate heading % symbol

    v = seperator.split(v[2])
    dens = float(v[1])
    num = int(v[2])
    elems = []
    for i in range(num):
        atomnum = int(v[3+i*2])
        ratio = float(v[4+i*2])
        elems.append((atomnum, ratio))

    return name, mass_percentage, dens, elems

if __name__ == '__main__':
    import sys
    tbl = parse(sys.stdin)

    for t in tbl:
        print '****'
        print t.desc
        print t.name
        print t.mass_percentage
        print t.elems
        print t.bonding
        print t.comment

