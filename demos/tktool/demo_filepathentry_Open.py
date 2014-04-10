import sys
import os
import tkinter as tk

__dir__ = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(__dir__, '../..'))

import suzu.tktool.filepathentry as filepathentry

if __name__ == '__main__':
    app = tk.Tk()

    fpath = filepathentry.Open(app)

    # operation
    # set
    def set_action():
        fpath.set('test string')

    setbtn = tk.Button(app, text='set', command=set_action)

    # get
    def get_action():
        print(fpath.get())

    getbtn = tk.Button(app, text='get', command=get_action)

    # clear
    def clear_action():
        fpath.clear()

    clearbtn = tk.Button(app, text='clear', command=clear_action)

    fpath.pack(side=tk.TOP, expand=True, fill=tk.X)
    setbtn.pack(side=tk.LEFT)
    getbtn.pack(side=tk.LEFT)
    clearbtn.pack(side=tk.LEFT)

    #fpath.grid(row=1, column=0, columnspan=3)
    #setbtn.grid(row=2, column=0)
    #getbtn.grid(row=2, column=1)
    #clearbtn.grid(row=2, column=2)

    app.mainloop()
