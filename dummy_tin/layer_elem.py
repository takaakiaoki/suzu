import tkinter as tk

from .physics import element as elem

from . import tktool
from .tktool import gui_abstract as ga
from .tktool import codedoptionmenu as coption
from .tktool import validateentry

from . import atomtbl

from . import context

class LayerElem(tk.Frame, ga.GUIAbstract):
    defaultparam = context.layer_elem_default
    exampleparam = context.layer_elem_example

    def __init__(self, master=None, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=self.defaultparam)

        prow = 0
        epadx = (15, 0) # x inner padding for Entries

        # name
        self.namefrm = tk.Frame(self)
        self.namelabel = tk.Label(self.namefrm, text='Layer Name')
        self.name = ga.TunedEntry(self.namefrm)
        self.add_widget('name', self.name)
        self.namelabel.grid(row=0, column=0, sticky=tk.SW)
        self.name.grid(row=1, column=0, padx=epadx, sticky=tk.NW)
        self.namefrm.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # width & wunit
        self.widthfrm = tk.Frame(self)
        # width
        self.widthlabel = tk.Label(self.widthfrm, text='Width')
        self.width = tktool.validateentry.DoublePositive(self.widthfrm, width=10, justify=tk.RIGHT)
        self.add_widget('width', self.width)
        # wunit
        self.wunitopts = [('Ang', 'Ang'), ('um', 'um'), ('mm', 'mm'),
                ('cm', 'cm'), ('m', 'm'), ('km', 'km')]
        self.wunit = coption.CodedOptionMenu(self.widthfrm, self.wunitopts)
        self.wunit.config(width=5)
        self.add_widget('wunit', self.wunit)

        self.widthlabel.grid(row=0, column=0, columnspan=2, sticky=tk.SW)
        self.width.grid(row=1, column=0, padx=epadx, sticky=tk.W)
        self.wunit.grid(row=1, column=1, sticky=tk.NW)
        self.widthfrm.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # dens
        self.densfrm = tk.Frame(self)
        self.denslabel = tk.Label(self.densfrm, text='Density (g/cm3)')
        self.dens = tktool.validateentry.DoublePositive(self.densfrm, width=10, justify=tk.RIGHT)
        self.add_widget('dens', self.dens)

        self.denslabel.grid(row=0, column=0, sticky=tk.SW)
        self.dens.grid(row=1, column=0, padx=epadx, sticky=tk.NW)

        self.densfrm.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # corr
        self.corrfrm = tk.Frame(self)
        self.corrlabel = tk.Label(self.corrfrm, text='Compound Corr.')
        self.corr = tktool.validateentry.DoublePositive(self.corrfrm, width=10, justify=tk.RIGHT)
        self.add_widget('corr', self.corr)

        self.corrlabel.grid(row=0, column=0, columnspan=3, sticky=tk.SW)
        self.corr.grid(row=1, column=0, padx=epadx, sticky=tk.NW)

        self.corrfrm.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # gas
        self.gas = ga.TunedCheckbuttonTF(self, text='Gas Material')
        self.add_widget('gas', self.gas)
        self.gas.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # atomtbl
        self.atomtblfrm = tk.LabelFrame(self, text='Atoms')
        self.atomtbl = atomtbl.AtomTbl(self.atomtblfrm)
        self.atomtbl.pack()
        self.add_widget('atomtbl', self.atomtbl)
        self.atomtblfrm.grid(row=0, column=4, rowspan=prow, padx=10)

        self.clear()



if __name__ == '__main__':
    from . import tktool

    app = tk.Tk()

    tktool.gui_testframe(app, LayerElem, LayerElem.exampleparam)

    app.mainloop()
