import Tkinter as tk

import tktool
import tktool.gui_abstract as ga
import tktool.validateentry
import tktool.codedoptionmenu as coption

class Param2(tk.LabelFrame, ga.GUIAbstract):
    defaultparam = {
            'ionrange':False,
            'bscatter':False,
            'transmit':0,
            'sputter':False,
            'collidetail':0,
            'einterval':0}
    exampleparam = {
            'ionrange':True,
            'bscatter':True,
            'transmit':1,
            'sputter':True,
            'collidetail':1,
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
        self.transmitframe = tk.Frame(self)
        self.transmitlabel = tk.Label(self.transmitframe, text='Transmitted Ions/Recoils')
        self.transmitopts = [
                (0,'0 = No file of Tranmitted Atoms'),
                (1,'1 = NEW file of Tranmitted Ions (TRANSMIT.txt)'),
                (2,'2 = APPEND to old file of TRANSMIT.txt'),
                (3,'3 = File of Transmitted Recoil Atoms (TRANSREC.txt)')
                ]
        self.transmit = coption.CodedOptionMenu(self.transmitframe, self.transmitopts)
        self.transmit.config(width=10, anchor=tk.W)
        self.add_widget('transmit', self.transmit)
        self.transmit.grid(row=0, column=0)
        self.transmitlabel.grid(row=0, column=1)
        self.transmitframe.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # sputter
        self.sputter = ga.TunedCheckbuttonTF(self, text='Sputtered Atoms')
        self.add_widget('sputter', self.sputter)
        self.sputter.grid(row=prow, column=0, sticky=tk.W)
        prow += 1

        # collidetail
        self.collidetailframe = tk.Frame(self)
        self.collidetaillabel = tk.Label(self.collidetailframe, text='Collision Details')
        self.collidetailopts = [
                (0,'0 = No file of Collision Details'),
                (1,'1 = Store Ion data to COLLISION.text'),
                (2,'2 = Store Ion and Recoil to COLLISION.txt (to heavy)')
                ]
        self.collidetail = coption.CodedOptionMenu(self.collidetailframe,
                self.collidetailopts)
        self.collidetail.config(width=10, anchor=tk.W)
        self.add_widget('collidetail', self.collidetail)
        self.collidetaillabel.grid(row=0, column=1)
        self.collidetail.grid(row=0, column=0)
        self.collidetailframe.grid(row=prow, column=0, sticky=tk.W)
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
