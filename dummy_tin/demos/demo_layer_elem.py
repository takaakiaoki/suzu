import sys
import os
import Tix as tix

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../..'))

import dummy_tin.layer_elem as layer_elem
import dummy_tin.tktool as tktool

if __name__ == '__main__':
    app = tix.Tk()

    tktool.gui_testframe(app, layer_elem.LayerElem, layer_elem.LayerElem.exampleparam)

    app.mainloop()
