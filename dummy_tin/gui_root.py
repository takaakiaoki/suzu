import Tkinter as tk

import tktool.gui_abstract as ga
import tktool.gui_testframe as gt

import tktool.codedoptionmenu as coption

class Root(tk.Frame, ga.GUIAbstract):
    defaultparam = {'damage':1, 'plots':0}
    exampleparam = {'damage':3, 'plots':4}

    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=Root.defaultparam)

        prow = 0

        # damage
        self.damageopts = [
            (1, '1:Ion Distrubution and Quick calculation of Damage.'),
            (2, '2:Detailed Calculation with Full Damage Cascades.'),
            (3, '3:Surface Sputtering / Monolayer Collision Steps')]
        self.damagelabel = tk.Label(self, text='Damage')
        self.damage = coption.CodedOptionMenu(self, self.damageopts)
        self.damage.config(width='50', anchor='w')
        self.add_widget('damage', self.damage)

        self.damagelabel.grid(row=prow, column=0)
        self.damage.grid(row=prow, column=1)
        prow += 1

        # Basic Plots
        self.plotsopts = [
            (0, '0:Ion Distribution with Recoils projected on Y-Plane'),
            (1, '1:Ion Distribution with Recoils projected on Z-Plane'),
            (2, '2:Recoil Distribution only (No Ions) projected on Y-Plane'),
            (3, '3:Transverse Plot of Ions + Recoil Cascades, YZ-Plane'),
            (4, '4:All FOUR of the above on one screen'),
            (5, '5:NO Graphics (Fastest Calc., or running TRIM in background)')]
        self.plotslabel = tk.Label(self, text='Basic Plots')
        self.plots = coption.CodedOptionMenu(self, self.plotsopts)
        self.plots.config(width='50', anchor='w')
        self.add_widget('plots', self.plots)

        self.plotslabel.grid(row=prow, column=0)
        self.plots.grid(row=prow, column=1)
        prow += 1

        self.clear()

if __name__ == '__main__':
    app = tk.Tk()

    gt.gui_testframe(app, Root, Root.exampleparam)

    app.mainloop()
