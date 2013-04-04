import Tkinter as tk

import physics.element as elem

import tktool
import tktool.gui_abstract as ga
import tktool.validateentry

class Proj(tk.Frame, ga.GUIAbstract):
    defaultparam = {'symbol':'H', 'z':1, 'w':1.008, 'energy':10, 'angle':0}
    exampleparam = {'symbol':'Si', 'z':14, 'w':29.977, 'energy':1000, 'angle':45}

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=Proj.defaultparam)

        # symbol
        self.symbollabel = tk.Label(self, text='Symbol')
        self.symbol = tktool.TruncatedEntry(self, limitwidth=2, width=3)
        self.add_widget('symbol', self.symbol)
        self.symbollabel.grid(row=0, column=0, sticky=tk.S)
        self.symbol.grid(row=1, column=0)

        # fill button
        self.fill = tk.Button(self, text='>', command=self.fill_by_type)
        self.fill.grid(row=1, column=1)

        # z
        self.zlabel = tk.Label(self, text='Atomic\nNumber')
        self.z = tktool.validateentry.IntPositive(self, width=5)
        self.add_widget('z', self.z)
        self.zlabel.grid(row=0, column=2, sticky=tk.S)
        self.z.grid(row=1, column=2)

        # w
        self.wlabel = tk.Label(self, text='Mass[amu]')
        self.w = tktool.validateentry.DoublePositive(self, width=8)
        self.add_widget('w', self.w)
        self.wlabel.grid(row=0, column=3, sticky=tk.S)
        self.w.grid(row=1, column=3)

        # energy
        self.energylabel = tk.Label(self, text='Energy[keV]')
        self.energy = tktool.validateentry.DoublePositive(self, width=10)
        self.add_widget('energy', self.energy)
        self.energylabel.grid(row=0, column=4, sticky=tk.S)
        self.energy.grid(row=1, column=4)

        # angle
        self.anglelabel = tk.Label(self, text='Angle of Incidence')
        self.angle = tktool.validateentry.Double(self, width=8)
        self.add_widget('angle', self.angle)
        self.anglelabel.grid(row=0, column=5, sticky=tk.S)
        self.angle.grid(row=1, column=5)

        self.clear()

    def fill_by_type(self):
        symbol = self.symbol.get()
        if symbol in elem.table_bysym:
            e = elem.table_bysym[symbol]
            self.z.set(e.z)
            self.w.set(e.mass)

    def enable(self):
        ga.GUIAbstract.enable(self)
        self.fill.config(state=tk.NORMAL)

    def disable(self):
        ga.GUIAbstract.disable(self)
        self.fill.config(state=tk.DISABLED)



if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Proj, Proj.exampleparam)

    app.mainloop()
