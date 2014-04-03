# coding: utf-8
""" parse SRIM compound database
"""

import io
import re

from ..physics import element as element
from ..db import disp as displacement

class Category(object):
    def __init__(self):
        self.desc = ''
        self.tables = []

    def get_title(self):
        """cut meanful category name from description strs """
        leadingchr = b'\xdf'.decode('cp437') # used for category in original compound.dat
        r = re.compile('{0:s}+\s*([^{0:s}]+?)\s*{0:s}+'.format(leadingchr))
        for l in self.desc.split('\n'):
            m = r.match(l)
            if m:
                return m.group(1)
        # if desc lines does not match, returns last line
        return l
        
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
        self.fulltext = '' # full text of table contents

    def to_suzu(self):
        """
        c: parsed object of srim compound data
        """

        # if ratio is given as mass percentage, transrate it
        table = []
        for z, r in self.elems:
            sym = element.table_bynum[z].sym
            w = element.table_bynum[z].mass
            if self.mass_percentage:
                r /= w
            table.append({
                'symbol':sym,
                'z':z,
                'w':w,
                'stoich':r,
                'disp':displacement.disp[sym]})

        layer = {
            'name': self.name,
            'dens': self.density,
            'atomtbl':table}

        return layer

def format_compound(c):
    """format contents of compounddb.Compound in Markdown like strucuture
    """

    def h1(text):
        sep = '=' * len(text)
        return '\n'.join((sep, text, sep)) + '\n'

    def h2(text):
        sep = '=' * len(text)
        return '\n'.join((text, sep)) + '\n'

    b = io.StringIO()
    # material title
    b.write(h1(c.name))
    # short description
    b.write('\n'+c.desc)
    # density
    b.write('\n'+h2('Density')+'\n')
    b.write('{0:g} g/cm3\n'.format(c.density))

    # components
    # number
    # symbol
    # atomic ratio
    # mass ratio
    b.write('\n'+h2('Elements and Ratio')+'\n')

    header   = ('Z', 'symbol', 'mass', 'atom ratio', 'mass ratio')
    colwidth = (  6,        6,      8,           12,          12)

    headerstr = [s.center(col) for col, s in zip(colwidth, header)]

    b.write(' | '.join(headerstr) + '\n')
    b.write('-+-'.join(['-'*cs for cs in colwidth]) + '\n')

    if c.mass_percentage:
        form = '{{0:{0:d}d}} | {{1:^{1:d}s}} | {{2:{2:d}g}} | {{3:{3:d}g}} | {{4:{4:d}g}}\n'.format(
                colwidth[0], colwidth[1], colwidth[2], colwidth[3], colwidth[4])
        for atomnum, ratio in c.elems:
            b.write(form.format(atomnum, element.table_bynum[atomnum].sym,
                element.table_bynum[atomnum].mass,
                ratio/element.table_bynum[atomnum].mass,
                ratio))
    else:
        form = '{{0:{0:d}d}} | {{1:^{1:d}s}} | {{2:{2:d}g}} | {{3:{3:d}g}} | {4:s}\n'.format(
                colwidth[0], colwidth[1], colwidth[2], colwidth[3], ' '*colwidth[4])
        for atomnum, ratio in c.elems:
            b.write(form.format(atomnum, element.table_bynum[atomnum].sym,
                element.table_bynum[atomnum].mass, ratio))

    b.write('\n')

    b.write('\n'+h2('Comment')+'\n')
    b.write(c.comment)

    b.write('\n'+h2('Original text')+'\n')
    b.write(c.fulltext)

    return b.getvalue()


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
                cat.append_table(parse_target_table(tblbuf))

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
                # pass to the parser..
                cat.append_table(parse_target_table(tblbuf))

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

def parse_target_table(s):
    """ parse input string for compound"""
    t = Compound()
    t.fulltext=s
    input = io.StringIO(s)
    # 1st line, description, remove heading '*'
    t.desc = input.readline()[1:]

    # 2nd line, name, density, elements
    t.name, t.mass_percentage, t.density, t.elems = parse_target_data(input.readline())

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

