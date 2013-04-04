import Tkinter as tk

import physics.element as elem

import tktool
import tktool.gui_abstract as ga
import tktool.gui_testframe as gt
import tktool.codedoptionmenu as coption
import tktool.validateentry

class Param1(tk.LabelFrame, ga.GUIAbstract):
    defaultparam = {
            'calcname':'',
            'autosave':10000,
            'totalion':99999,
            'randseed':0,
            'windowmin':0,
            'windowmax':0}
    exampleparam = {
            'calcname':'suzu test',
            'autosave':100,
            'totalion':1,
            'randseed':117,
            'windowmin':100,
            'windowmax':1000}

    def __init__(self, master, *args, **kw):
        tk.LabelFrame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=Param1.defaultparam)

        # calcuname
        self.calcnamelabel = tk.Label(self, text='Name of Calculation')
        self.calcname = ga.TunedEntry(self, width=40)
        self.add_widget('calcname', self.calcname)
        self.calcnamelabel.grid(row=0, column=0, columnspan=4, sticky=tk.W)
        self.calcname.grid(row=1, column=0, columnspan=4, sticky=tk.E)

        # autosave
        self.autosavelabel = tk.Label(self, text='AutoSave at Ion #')
        self.autosave = tktool.validateentry.IntPositive(self, width=8, justify=tk.RIGHT)
        self.add_widget('autosave', self.autosave)
        self.autosavelabel.grid(row=2, column=0, sticky=tk.W)
        self.autosave.grid(row=2, column=1, sticky=tk.W+tk.E)

        # totalion
        self.totalionlabel = tk.Label(self, text='Total Number of Ions')
        self.totalion = tktool.validateentry.IntPositive(self, width=8, justify=tk.RIGHT)
        self.add_widget('totalion', self.totalion)
        self.totalionlabel.grid(row=3, column=0, sticky=tk.W)
        self.totalion.grid(row=3, column=1, sticky=tk.W+tk.E)

        # randseed
        self.randseedlabel = tk.Label(self, text='Random Number Seed')
        self.randseed = tktool.validateentry.IntZeroPositive(self, width=8, justify=tk.RIGHT)
        self.add_widget('randseed', self.randseed)
        self.randseedlabel.grid(row=4, column=0, sticky=tk.W)
        self.randseed.grid(row=4, column=1, sticky=tk.W+tk.E)

        # Plotting Window Depth
        self.pwindowmesglabel = tk.Label(self, text='Plotting Window Depths')
        self.pwindowmesglabel.grid(row = 2, column=2, columnspan=2, padx=5)

        # windowmin
        self.windowminlabel = tk.Label(self, text='Min (Ang)')
        self.windowmin = tktool.validateentry.IntZeroPositive(self, width=8, justify=tk.RIGHT)
        self.add_widget('windowmin', self.windowmin)
        self.windowminlabel.grid(row=3, column=2, sticky=tk.E, padx=5)
        self.windowmin.grid(row=3, column=3, sticky=tk.W+tk.E)

        # windowmax
        self.windowmaxlabel = tk.Label(self, text='Max (Ang)')
        self.windowmax = tktool.validateentry.IntZeroPositive(self, width=8, justify=tk.RIGHT)
        self.add_widget('windowmax', self.windowmax)
        self.windowmaxlabel.grid(row=4, column=2, sticky=tk.E, padx=5)
        self.windowmax.grid(row=4, column=3, sticky=tk.W+tk.E)

        self.clear()

if __name__ == '__main__':
    app = tk.Tk()

    gt.gui_testframe(app, Param1, Param1.exampleparam)

    app.mainloop()
