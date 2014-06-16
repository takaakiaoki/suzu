"""
table of element
"""

class AtomData(object):
    def __init__(self, name, symbol, number, mass):
        self.name = name
        self.sym = symbol
        self.z = number
        self.mass = mass

# elements
Ac = AtomData( "actinium",      "Ac",   89, 227 )
Ag = AtomData( "silver",        "Ag",   47, 107.8682 )
Al = AtomData( "aluminium",     "Al",   13, 26.981538 )
Am = AtomData( "americium",     "Am",   95, 243 )
Ar = AtomData( "argon",         "Ar",   18, 39.948 )
As = AtomData( "arsenic",       "As",   33, 74.9216 )
At = AtomData( "astatine",      "At",   85, 210 )
Au = AtomData( "gold",          "Au",   79, 196.96655 )
B  = AtomData( "boron",         "B",     5, 10.811 )
Ba = AtomData( "barium",        "Ba",   56, 137.327 )
Be = AtomData( "beryllium",     "Be",    4, 9.012182 )
Bh = AtomData( "bohrium",       "Bh",  107, 264 )
Bi = AtomData( "bismuth",       "Bi",   83, 208.98038 )
Bk = AtomData( "berkelium",     "Bk",   97, 247 )
Br = AtomData( "bromine",       "Br",   35, 79.904 )
C  = AtomData( "carbon",        "C",     6, 12.0107 )
Ca = AtomData( "calcium",       "Ca",   20, 40.078 )
Cd = AtomData( "cadmium",       "Cd",   48, 112.411 )
Ce = AtomData( "cerium",        "Ce",   58, 140.116 )
Cf = AtomData( "californium",   "Cf",   98, 251 )
Cl = AtomData( "chlorine",      "Cl",   17, 35.4527 )
Cm = AtomData( "curium",        "Cm",   96, 247 )
Cn = AtomData( "Copernicium",   "Cn",  112, 277 )
Co = AtomData( "cobalt",        "Co",   27, 58.9332 )
Cr = AtomData( "chromium",      "Cr",   24, 51.9961 )
Cs = AtomData( "caesium",       "Cs",   55, 132.90545 )
Cu = AtomData( "copper",        "Cu",   29, 63.546 )
Db = AtomData( "dubnium",       "Db",  105, 262 )
Ds = AtomData( "darmstadtium",  "Ds",  110, 269 )
Dy = AtomData( "dysprosium",    "Dy",   66, 162.5 )
Er = AtomData( "erbium",        "Er",   68, 167.26 )
Es = AtomData( "einsteinium",   "Es",   99, 252 )
Eu = AtomData( "europium",      "Eu",   63, 151.964 )
F  = AtomData( "fluorine",      "F",     9, 18.9984032 )
Fe = AtomData( "iron",          "Fe",   26, 55.845 )
Fl = AtomData('flerovium', 'Fl', 114, 289)
Fm = AtomData( "fermium",       "Fm",  100, 257 )
Fr = AtomData( "francium",      "Fr",   87, 223 )
Ga = AtomData( "gallium",       "Ga",   31, 69.723 )
Gd = AtomData( "gadolinium",    "Gd",   64, 157.25 )
Ge = AtomData( "germanium",     "Ge",   32, 72.61 )
H  = AtomData( "hydrogen",      "H",     1, 1.00794 )
He = AtomData( "helium",        "He",    2, 4.002602 )
Hf = AtomData( "hafnium",       "Hf",   72, 178.49 )
Hg = AtomData( "mercury",       "Hg",   80, 200.59 )
Ho = AtomData( "holmium",       "Ho",   67, 164.93032 )
Hs = AtomData( "hassium",       "Hs",  108, 269 )
I  = AtomData( "iodine",        "I",    53, 126.90447 )
In = AtomData( "indium",        "In",   49, 114.818 )
Ir = AtomData( "iridium",       "Ir",   77, 192.217 )
K  = AtomData( "potassium",     "K",    19, 39.0983 )
Kr = AtomData( "krypton",       "Kr",   36, 83.8 )
La = AtomData( "lanthanum",     "La",   57, 138.9055 )
Li = AtomData( "lithium",       "Li",    3, 6.941 )
Lr = AtomData( "lawrencium",    "Lr",  103, 262 )
Lu = AtomData( "lutetium",      "Lu",   71, 174.967 )
Lv = AtomData('livermorium', 'Lv', 116, 293)
Md = AtomData( "mendelevium",   "Md",  101, 258 )
Mg = AtomData( "magnesium",     "Mg",   12, 24.305 )
Mn = AtomData( "manganese",     "Mn",   25, 54.938049 )
Mo = AtomData( "molybdenum",    "Mo",   42, 95.94 )
Mt = AtomData( "meitnerium",    "Mt",  109, 268 )
N  = AtomData( "nitrogen",      "N",     7, 14.00674 )
Na = AtomData( "sodium",        "Na",   11, 22.98977 )
Nb = AtomData( "niobium",       "Nb",   41, 92.90638 )
Nd = AtomData( "neodymium",     "Nd",   60, 144.24 )
Ne = AtomData( "neon",          "Ne",   10, 20.1797 )
Ni = AtomData( "nickel",        "Ni",   28, 58.6934 )
No = AtomData( "nobelium",      "No",  102, 259 )
Np = AtomData( "neptunium",     "Np",   93, 237 )
O  = AtomData( "oxygen",        "O",     8, 15.9994 )
Os = AtomData( "osmium",        "Os",   76, 190.23 )
P  = AtomData( "phosphorus",    "P",    15, 30.973762 )
Pa = AtomData( "protactinium",  "Pa",   91, 231.03588 )
Pb = AtomData( "lead",          "Pb",   82, 207.2 )
Pd = AtomData( "palladium",     "Pd",   46, 106.42 )
Pm = AtomData( "promethium",    "Pm",   61, 145 )
Po = AtomData( "polonium",      "Po",   84, 210 )
Pr = AtomData( "praseodymium",  "Pr",   59, 140.90765 )
Pt = AtomData( "platinum",      "Pt",   78, 195.078 )
Pu = AtomData( "plutonium",     "Pu",   94, 244 )
Ra = AtomData( "radium",        "Ra",   88, 226 )
Rb = AtomData( "rubidium",      "Rb",   37, 85.4678 )
Re = AtomData( "rhenium",       "Re",   75, 186.207 )
Rf = AtomData( "rutherfordium", "Rf",  104, 261 )
Rg = AtomData( "roentgenium",   "Rg",  111, 272 )
Rh = AtomData( "rhodium",       "Rh",   45, 102.9055 )
Rn = AtomData( "radon",         "Rn",   86, 222 )
Ru = AtomData( "ruthenium",     "Ru",   44, 101.07 )
S  = AtomData( "sulphur",       "S",    16, 32.066 )
Sb = AtomData( "antimony",      "Sb",   51, 121.76 )
Sc = AtomData( "scandium",      "Sc",   21, 44.95591 )
Se = AtomData( "selenium",      "Se",   34, 78.96 )
Sg = AtomData( "seaborgium",    "Sg",  106, 266 )
Si = AtomData( "silicon",       "Si",   14, 28.0855 )
Sm = AtomData( "samarium",      "Sm",   62, 150.36 )
Sn = AtomData( "tin",           "Sn",   50, 118.71 )
Sr = AtomData( "strontium",     "Sr",   38, 87.62 )
Ta = AtomData( "tantalum",      "Ta",   73, 180.9479 )
Tb = AtomData( "terbium",       "Tb",   65, 158.92534 )
Tc = AtomData( "technetium",    "Tc",   43, 98 )
Te = AtomData( "tellurium",     "Te",   52, 127.6 )
Th = AtomData( "thorium",       "Th",   90, 232.0381 )
Ti = AtomData( "titanium",      "Ti",   22, 47.867 )
Tl = AtomData( "thallium",      "Tl",   81, 204.3833 )
Tm = AtomData( "thulium",       "Tm",   69, 168.93421 )
U  = AtomData( "uranium",       "U",    92, 238.0289 )
Uuo = AtomData('ununoctium', 'Uuo', 118, 294)
Uup = AtomData('ununpentium', 'Uup', 115, 288)
Uus = AtomData('ununseptium', 'Uus', 117, 294)
Uut = AtomData( 'ununtrium', 'Uut', 113, 284)
V  = AtomData( "vanadium",      "V",    23, 50.9415 )
W  = AtomData( "tungsten",      "W",    74, 183.84 )
Xe = AtomData( "xenon",         "Xe",   54, 131.29 )
Y  = AtomData( "yttrium",       "Y",    39, 88.90585 )
Yb = AtomData( "ytterbium",     "Yb",   70, 173.04 )
Zn = AtomData( "zinc",          "Zn",   30, 65.39 )
Zr = AtomData( "zirconium",     "Zr",   40, 91.224 )


None_ = AtomData( "none", "None", 0, 0 )

"table by atomic number"
table_bynum = [
        None_,
        H,                          He,
        Li, Be, B,  C,  N,  O,  F,  Ne,
        Na, Mg, Al, Si, P,  S,  Cl, Ar,
        K,  Ca, Sc, Ti, V,  Cr, Mn, Fe, Co, Ni, Cu, Zn,
        Ga, Ge, As, Se, Br, Kr,
        Rb, Sr, Y,  Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd,
        In, Sn, Sb, Te, I,  Xe,
        Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb,
        Lu, Hf, Ta, W,  Re, Os, Ir, Pt, Au, Hg,
        Tl, Pb, Bi, Po, At, Rn,
        Fr, Ra, Ac, Th, Pa, U,  Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No,
        Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Uut,Fl, Uup,Lv, Uus,Uuo]

"table by symbol"
table_bysym = dict([(a.sym, a) for a in table_bynum])

"table by name"
table_byname = dict([(a.name, a) for a in table_bynum])

if __name__ == '__main__':
    import sys
    for a in sys.argv[1:]:
        elem = None
        if a.lower() in table_byname:
            elem = table_byname[a]
        elif a in table_bysym:
            elem = table_bysym[a]
        else:
            try:
                n = int(a)
                if 0 < n < len(table_bynum):
                    elem = table_bynum[n]
            except:
                pass

        if elem:
            print('----')
            print(elem.name)
            print(elem.sym)
            print(elem.z)
            print(elem.mass)
