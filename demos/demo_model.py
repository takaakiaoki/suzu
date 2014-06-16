import sys
import os
import tkinter as tk

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..'))

import suzu.model as model
import suzu.tktool as tktool

if __name__ == '__main__':
    app = tk.Tk()

    tktool.gui_testframe(app, model.Model, model.Model.exampleparam)

    app.mainloop()
