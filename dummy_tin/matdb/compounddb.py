# coding: utf-8
""" parse SRIM compound data base
"""

import cStringIO
import re

class Category(object):
    def __init__(self):
        self.desc = ''
        self.tables = []

    def get_title(self):
        """cut meanful category name from description strs """
        r = re.compile('\xdf+\s*([^\xdf]+?)\s*\xdf+')
        for l in self.desc.split('\n'):
            m = r.match(l)
            if m:
                return m.group(1)
        return ''
        
    def append_table(self, tbl):
        self.tables.append(tbl)

class Compound(object):
    def __init__(self):
        self.desc = '' # target description
        self.name = '' # name of table
        self.mass_percentage = False # F: atom%, T: mass%
        self.density = 0.0 #density
        self.elems = []  # (atomnum, atom or mass%)
        self.bonding = [0.0] * 18 
        self.comment = ''

def parse(input):
    """parse into tables
    """
    ST_UNDEFINED = 0
    ST_CAT_DESC = 1
    ST_TBL_DATA = 2

    state = ST_UNDEFINED

    categories = []

    cat = Category()
    catbuf = ''
    tblbuf = ''

    """
              \  !                     |   *                       |   else
    UNDEFINED |  append_cat.desc/C     |   append_tblbuf/T         |  -
    CAT_DESC  |  append_cat.desc/C     |   append_tblbuf/T         |  - 
    TBL_DATA  |  parse_tbl,push_cat/C  |   parse_tbl,push_to_cat/T |  append_tblbuf/T
    """

    for line in input.readlines():
        if line[0] == '!':
            if state == ST_TBL_DATA:
                # close buffer and parse the contentents
                toparse = cStringIO.StringIO(tblbuf)
                # pass to the parser..
                cat.append_table(parse_target_table(toparse))

                # clear tbl buffer
                tblbuf = ''

                # prepare new category
                categories.append(cat)
                cat = Category()
                cat.desc += line[1:]
            elif state == ST_CAT_DESC or state == ST_UNDEFINED:
                # append description line
                cat.desc += line[1:]
            state = ST_CAT_DESC

        elif line[0] == '*':
            if state == ST_TBL_DATA:
                # close buffer and parse the contentents
                toparse = cStringIO.StringIO(tblbuf)
                # pass to the parser..
                cat.append_table(parse_target_table(toparse))

                # enter new target entry
                tblbuf = line
            else:
                # enter new target entry
                tblbuf = line
            state = ST_TBL_DATA

        else: # other line
            if state == ST_TBL_DATA:
                tblbuf += line

    if cat.tables:
        categories.append(cat)

    return categories

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

    cat = parse(sys.stdin)

    for c in cat:
        print '!!!!!'
        #print c.desc
        print c.get_title()

        for t in c.tables:
            print '****'
            #print t.desc
            print t.name
            print t.density
            print t.mass_percentage
            print t.elems
            print t.bonding
            print t.comment

