import sys
import os
import tkinter.tix as tix

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..'))

import suzu.layer_elem as layer_elem
import suzu.tktool as tktool

if __name__ == '__main__':
    app = tix.Tk()

    tktool.gui_testframe(app, layer_elem.LayerElem, layer_elem.LayerElem.exampleparam)

    app.mainloop()
