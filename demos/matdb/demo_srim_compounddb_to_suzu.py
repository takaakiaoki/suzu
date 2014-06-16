# coding: utf-8
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../..'))

import suzu.matdb.srim_compounddb as compounddb

air = compounddb.Compound()

air.desc = 'Air, Dry near sea level (ICRU-104)  0.00120484  O-23.2, N-75.5, Ar-1.3'
air.name = '%Air, Dry (ICRU-104)'
air.density = 0.00120484
air.mass_percentage = True
air.elems = [(6, 0.000124), (8, 0.231781), (7, 0.755267), (18, 0.012827)]
air.bonding = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
air.comment = """corrected by H. Paul, Sept. 2004
"""
air.fulltext = """*Air, Dry near sea level (ICRU-104)  0.00120484  O-23.2, N-75.5, Ar-1.3
"%Air, Dry (ICRU-104)", .00120484, 4, 6, .000124, 8, .231781, 7, .755267, 18, .012827
0 0 0 0   0 0 0 0 0 0 0 0   0 0 0   0 0 0
$ corrected by H. Paul, Sept. 2004
$"""

water = compounddb.Compound()

water.desc = 'Water  (liquid)                     1.00        H-2, O-1'
water.name = 'Water_Liquid (ICRU-276)'
water.density = 1.0
water.mass_percentage = False
water.elems = [(1, 2.0), (8, 1.0)]
water.bonding = [0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
water.comment = b"""Chemical Formula:      H \u00c4\u00c4 O \u00c4\u00c4 H

There is about an 8% increase in the peak of the stopping power
for ions in water vapour relative to the liquid. (The peak of the
stopping occurs at an energy of about 100 keV/amu times the 2/3
power of the ion's atomic number.) Above the peak the phase
difference begins to disappear. This calculation is for the
LIQUID phase. """.decode('cp437')

print(water.to_suzu())
print(air.to_suzu())
