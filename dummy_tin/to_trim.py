def t1(d):
    s = '{z:d} {w:f} {energy:f} {angle:f} {totalion:d} 1 {autosave:d}'.format(
            z = d['proj']['z'],
            w = d['proj']['w'],
            energy = d['proj']['energy'],
            angle = d['proj']['angle'],
            totalion = d['param1']['totalion'],
            autosave = d['param1']['autosave']
            )
    return s

def t2(d):
    s = '{damage:d} {randseed:d} 0'.format(
            damage = d['damage'],
            randseed = d['param1']['randseed']
            )
    return s

def t3(d):
    s = '{ionrange:d} {bscatter:d} {transmit:d} {sputter:d} {collidetail:d} {einterval:f}'.format(**d['param2'])
    return s

def t4(d):
    # trim calcname in 40 chars
    s = '"{0:<40s}" {1:d} {2:d}'.format(d['param1']['calcname'],
            d['tatoms'], d['tlayers'])
    return s

def t5(d):
    # trim calcname in 40 chars
    s = '{0:d} {1:f} {2:f}'.format(d['plots'],
            d['param1']['windowmin'], d['param1']['windowmax'])
    return s

def t6(d):
    ss = []
    for i, a in enumerate(d['linatomtbl'], 1):
        s1 = 'Atom{0:2d} = {1:s} ='.format(i, a['symbol'])
        s = '{0:14s} {1:d} {2:f}'.format(s1, a['z'], a['w'])
        ss.append(s)
    return '\n'.join(ss)

def t7(d):
    ss = []
    for i, a in enumerate(d['linatomtbl'], 1):
        s = '{0:>7s}'.format('{symbol:s}({z:d})'.format(**a))
        ss.append(s)
    return ''.join(ss)

def t8(d):
    return ' Stoich' * d['tatoms']

def t9(d):
    #stoich table
    allstotbl = []
    sidx = 0
    for lay in d['layer']:
        sto = [0.0] * d['tatoms']
        # set sto[sidx:sidx+latoms]
        latoms = len(lay['atomtbl'])
        s = 0.0
        for i, a in enumerate(lay['atomtbl'], sidx):
            sto[i] = a['stoich']
            s += a['stoich']

        for i in range(sidx, latoms):
            sto[i] /= s

        allstotbl.append(sto[:])
        sidx += latoms

    # format and output
    ss = []
    unittrans = {
            'Ang':1,
            'um':1e4,
            'mm':1e7,
            'cm':1e8,
            'm':1e10,
            'km':1e13
            }
    for i, (lay, sto) in enumerate(zip(d['layer'], allstotbl), 1):
        s = '{0:2d} "{1:s}" {2:f} {3:f} {4:s}'.format(
                i,
                lay['name'],
                lay['width']*unittrans[lay['wunit']],
                lay['dens'],
                ' '.join(['{0:f}'.format(v) for v in sto]))
        ss.append(s)

    return '\n'.join(ss)

def t10(d):
    return ' '.join(['{0:d}'.format(v['gas']) for v in d['layer']])

def t11(d):
    return ' '.join(['{0:f}'.format(v['corr']) for v in d['layer']])

def t12(d):
    return ' '.join(['{0:f}'.format(a['disp'][0]) for a in d['linatomtbl']])

def t13(d):
    return ' '.join(['{0:f}'.format(a['disp'][1]) for a in d['linatomtbl']])

def t14(d):
    return ' '.join(['{0:f}'.format(a['disp'][2]) for a in d['linatomtbl']])

template = \
"""==> SRIM-2013.00 This file controls TRIM Calculations.
Ion: Z1 ,  M1,  Energy (keV), Angle,Number,Bragg Corr,AutoSave Number.
{t1:s}
Cascades(1=No;2=Full;3=Sputt;4-5=Ions;6-7=Neutrons), Random Number Seed, Reminders
{t2:s}
Diskfiles (0=no,1=yes): Ranges, Backscatt, Transmit, Sputtered, Collisions(1=Ion;2=Ion+Recoils), Special EXYZ.txt file
{t3:s}
Target material : Number of Elements & Layers
{t4:s}
PlotType (0-5); Plot Depths: Xmin, Xmax(Ang.) [=0 0 for Viewing Full Target]
{t5:s}
Target Elements:    Z   Mass(amu)
{t6:s}
Layer   Layer Name /               Width Density   {t7:s}
Numb.   Description                (Ang) (g/cm3)   {t8:s}
{t9:s}
0  Target layer phases (0=Solid, 1=Gas)
{t10:s}
Target Compound Corrections (Bragg)
{t11:s}
Individual target atom displacement energies (eV)
{t12:s}
Individual target atom lattice binding energies (eV)
{t13:s}
Individual target atom surface binding energies (eV)
{t14:s}
Stopping Power Version (1=2011, 0=2011)
 0 
"""

def to_trim(d, stream):
    # linealize atomtable
    linatomtbl = []
    for lay in d['layer']:
        linatomtbl += lay['atomtbl']

    d['linatomtbl'] = linatomtbl

    # get total layer and atoms
    d['tlayers'] = len(d['layer'])
    d['tatoms'] = len(linatomtbl)


    s = template.format(t1=t1(d), t2=t2(d), t3=t3(d), t4=t4(d), t5=t5(d),
            t6=t6(d), t7=t7(d), t8=t8(d), t9=t9(d), t10=t10(d),
            t11=t11(d), t12=t12(d), t13=t13(d), t14=t14(d))
    stream.write(s)

if __name__ == '__main__':
    import sys
    import root

    # print root.Root.exampleparam

    to_trim(root.Root.exampleparam, sys.stdout)
