import Tkinter as tk

import tktool
import tktool.gui_abstract as ga
import tktool.validateentry

class Param2(tk.LabelFrame, ga.GUIAbstract):
    defaultparam = {
            'ionrange':False,
            'bscatter':False,
            'transmit':False,
            'sputter':False,
            'collidetail':False,
            'einterval':0}
    exampleparam = {
            'ionrange':True,
            'bscatter':True,
            'transmit':True,
            'sputter':True,
            'collidetail':True,
            'einterval':25}

    def __init__(self, master, *args, **kw):
        tk.LabelFrame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=Param2.defaultparam)

        self.config(text='Output Disk Files')
    
        prow = 0

        # ionrange
        self.ionrange = ga.TunedCheckbuttonTF(self, text='Ion Ranges')
        self.add_widget('ionrange', self.ionrange)
        self.ionrange.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # bscatter
        self.bscatter = ga.TunedCheckbuttonTF(self, text='Backscattered Ions')
        self.add_widget('bscatter', self.bscatter)
        self.bscatter.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # transmit
        self.transmit = ga.TunedCheckbuttonTF(self, text='Transmitted Ions/Recoils')
        self.add_widget('transmit', self.transmit)
        self.transmit.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # sputter
        self.sputter = ga.TunedCheckbuttonTF(self, text='Sputtered Atoms')
        self.add_widget('sputter', self.sputter)
        self.sputter.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # collidetail
        self.collidetail = ga.TunedCheckbuttonTF(self, text='Collision Details')
        self.add_widget('collidetail', self.collidetail)
        self.collidetail.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # einterval
        self.eintframe = tk.Frame(self)
        self.eintervallabel = tk.Label(self.eintframe, text='Special "EXYZ File" Increment(eV)')
        self.einterval = tktool.validateentry.Double(self.eintframe, width=10, justify=tk.RIGHT)
        self.add_widget('einterval', self.einterval)
        self.eintervallabel.grid(row=0, column=1)
        self.einterval.grid(row=0, column=0)

        self.eintframe.grid(row=prow, column=0, sticky=tk.W)
        
        self.clear()

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Param2, Param2.exampleparam)

    app.mainloop()
