import Tkinter as tk

import tktool.oneof

import layer_elem

import context

defaultparam = context.layer_default
exampleparam = context.layer_example

layout = {
        # ctrl frame, relative to root frame
        'ctrl':{'row':0, 'column':0, 'sticky':tk.NE, 'padx':(0,10)},
        # element view, relative to root frame
        'view':{'row':0, 'column':1, 'sticky':tk.W},
        # control parts which are placed in ctrlfrm in usual
        # if a widget should be placed in relative to root frame
        # set 'root' for key 'in', otherwise it is placed in ctrl frame
        'index':{'in':'ctrl', 'row':0, 'column':0, 'sticky':tk.W},
        'totallabel':{'row':0, 'column':1, 'sticky':tk.W}, # 'in' key can be ommitted.
        'append':{'row':1, 'column':0, 'columnspan':2, 'sticky':tk.EW},
        'delete':{'row':2, 'column':0, 'columnspan':2, 'sticky':tk.EW}
        }

Layer = tktool.oneof.OneofFactory(layer_elem.LayerElem,
        layer_elem.LayerElem.defaultparam,
        layout)

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Layer, exampleparam)

    app.mainloop()
