import tkinter as tk

from . import tktool
from .tktool import oneof

from . import layer_elem

from . import context

defaultparam = context.target_default
exampleparam = context.target_example

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
        'append':{'row':1, 'column':0, 'columnspan':2, 'pady':(10,0), 'sticky':tk.EW},
        'delete':{'row':2, 'column':0, 'columnspan':2, 'sticky':tk.EW}
        }

TargetBase = tktool.oneof.OneofFactory(layer_elem.LayerElem,
        layer_elem.LayerElem.defaultparam,
        layout)

class Target(TargetBase):
    def __init__(self, master=None, gridlayout=None, *args, **kw):
        TargetBase.__init__(self, master, gridlayout, *args, **kw)

    def validate(self):
        if self.is_disabled():
            return None

        # 1st level validation for each widget
        err = TargetBase.validate(self)
        if err:
            return err

        err = []
        errorlayers = []

        # 2nd level validation 
        # sum of stoich not should be 0
        # store current view, it must pass because contents of
        # view is already validated
        self.store_currentview()
        for i, edata in enumerate(self.elemdata):
            ss = 0.0
            if 'atomtbl' in edata:
                for e in edata['atomtbl']:
                    ss += e['stoich']
            if ss < 1e-6:
                errorlayers.append(i)
                err.append(('layer {0:d}'.format(i+1),
                    'sum of stoich. is zero (or too small)'))

        if err:
            # set first error layer on view and set alert face
            self.index_action_force(errorlayers[0])
            # set alert on stoich column
            self.view.atomtbl.alert_stoich_column()
        else:
            # clear alert on stoich column 
            self.view.atomtbl.noalert_stoich_column()

        return err if err else None



if __name__ == '__main__':
    from . import tktool
    import copy

    app = tk.Tk()

    ex2 = copy.deepcopy(exampleparam)

    # example 2 stoichimetry of layer 2 is too small
    ex2[1]['atomtbl'][0]['stoich'] = 0
    ex2[1]['atomtbl'][1]['stoich'] = 0

    examples = [('standard', exampleparam),
            ('stoich. error in 2nd layer', ex2)]

    tktool.gui_testframe_multiexam(app, Target, examples)

    app.mainloop()
