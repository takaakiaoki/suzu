import Tkinter as tk

import physics.element as elem

import tktool
import tktool.gui_abstract as ga
import tktool.codedoptionmenu as coption
import tktool.validateentry

class LayerElem(tk.Frame, ga.GUIAbstract):
    defaultparam = {
            'name':'Layer',
            'width': 100000,
            'wunit': 'Ang',
            'dens': 0.0,
            'corr': 1.0,
            'gas': False
            }
    exampleparam = {
            'name':'Silicon',
            'width': 100000,
            'wunit': 'um',
            'dens': 2.312,
            'corr': 1.0,
            'gas': True
            }

    def __init__(self, master=None, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=LayerElem.defaultparam)

        prow = 0

        # name
        self.namelabel = tk.Label(self, text='Layer Name')
        self.name = ga.TunedEntry(self)
        self.add_widget('name', self.name)
        self.namelabel.grid(row=prow, column=0, columnspan=3, sticky=tk.W)
        prow += 1
        # dummy frame
        tk.Frame(self).grid(row=prow, column=0, ipadx=5)
        self.name.grid(row=prow, column=1, columnspan=2, sticky=tk.W)
        prow += 1

        # fill very small space
        tk.Frame(self).grid(row=prow, column=0, ipady=3)
        prow += 1

        # width
        self.widthlabel = tk.Label(self, text='Width')
        self.width = tktool.validateentry.DoublePositive(self, width=10, justify=tk.RIGHT)
        self.add_widget('width', self.width)
        self.widthlabel.grid(row=prow, column=0, columnspan=3, sticky=tk.W)
        prow += 1
        self.width.grid(row=prow, column=1, sticky=tk.W)

        # wunit
        self.wunitopts = [('Ang', 'Ang'), ('um', 'um'), ('mm', 'mm'),
                ('cm', 'cm'), ('m', 'm'), ('km', 'km')]

        self.wunit = coption.CodedOptionMenu(self, self.wunitopts)
        self.wunit.config(width=5)
        self.add_widget('wunit', self.wunit)
        self.wunit.grid(row=prow, column=2, sticky=tk.W)
        prow += 1

        # dens
        self.denslabel = tk.Label(self, text='Density (g/cm3)')
        self.dens = tktool.validateentry.DoublePositive(self, width=10, justify=tk.RIGHT)
        self.add_widget('dens', self.dens)
        self.denslabel.grid(row=prow, column=0, columnspan=3, sticky=tk.W)
        prow += 1
        self.dens.grid(row=prow, column=1, sticky=tk.W)
        prow += 1

        # corr
        self.corrlabel = tk.Label(self, text='Compound Corr.')
        self.corr = tktool.validateentry.DoublePositive(self, width=10, justify=tk.RIGHT)
        self.add_widget('corr', self.corr)
        self.corrlabel.grid(row=prow, column=0, columnspan=3, sticky=tk.W)
        prow += 1
        self.corr.grid(row=prow, column=1, sticky=tk.W)
        prow += 1
        self.clear()

        # gas
        self.gas = ga.TunedCheckbuttonTF(self, text='Gas Material')
        self.add_widget('gas', self.gas)
        self.gas.grid(row=prow, column=0, columnspan=3, sticky=tk.W)

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, LayerElem, LayerElem.exampleparam)

    app.mainloop()
