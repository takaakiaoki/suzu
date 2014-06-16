import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../..')))

import tkinter.tix as tix

# import suzu
import suzu.matdb.srim_matdb_frame as srim_matdb_frame
import suzu.matdb.srim_compounddb as compounddb

if __name__ == '__main__':
    app = tix.Tk()

    datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'Compound.dat'))

    top = tix.Toplevel()
    d = srim_matdb_frame.SRIMMatDBFrame(top, datapath)

    d.grid(row=0, column=0, sticky=tix.N+tix.E+tix.S+tix.W)
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    def c():
        print(d.dselect.get_current_selection())

    tix.Button(app, text='get value', command=c).pack()

    top.wait_window()

    app.mainloop()
