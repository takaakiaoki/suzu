import Tkinter as tk

import tktool.oneof

import layer_elem

defaultparam = [layer_elem.LayerElem.defaultparam]
exampleparam = [
        {'name':'Silicon', 'width':100, 'wunit':'Ang', 'dens':2.3212,
            'corr':1.0, 'gas':False},
        {'name':'Water', 'width':1, 'wunit':'um', 'dens':0.00125,
            'corr':0.94, 'gas':True},
        ]

Layer = tktool.oneof.OneofFactory(layer_elem.LayerElem,
        layer_elem.LayerElem.defaultparam)

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Layer, exampleparam)

    app.mainloop()
