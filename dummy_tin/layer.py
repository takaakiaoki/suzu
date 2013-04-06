import Tkinter as tk

import tktool.oneof

import layer_elem

import context

defaultparam = context.layer_default
exampleparam = context.layer_example

Layer = tktool.oneof.OneofFactory(layer_elem.LayerElem,
        layer_elem.LayerElem.defaultparam)

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Layer, exampleparam)

    app.mainloop()
