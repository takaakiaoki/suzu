import Tkinter as tk

import tktool.oneof

import layer_elem

defaultparam = [layer_elem.LayerElem.defaultparam]
exampleparam = [
        {'name':'Silicon', 'width':100, 'wunit':'Ang', 'dens':2.3212,
            'corr':1.0, 'gas':False,
            'atomtbl':[
                {'symbol':'Si', 'z':14, 'w':28.088,
                    'stoich':1, 'disp':[15, 2, 4.7]}]},
        {'name':'Water', 'width':1, 'wunit':'um', 'dens':0.00125,
            'corr':0.94, 'gas':True,
            'atomtbl':[
                {'symbol':'H', 'z':1, 'w':1.008, 'stoich':2,
                    'disp':[10, 3, 2]},
                {'symbol':'O', 'z':8, 'w':15.999, 'stoich':1,
                    'disp':[28, 3, 2]}]}
        ]

Layer = tktool.oneof.OneofFactory(layer_elem.LayerElem,
        layer_elem.LayerElem.defaultparam)

if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, Layer, exampleparam)

    app.mainloop()
