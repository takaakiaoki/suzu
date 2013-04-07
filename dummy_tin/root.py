import Tkinter as tk

import tktool.gui_abstract as ga

import tktool.codedoptionmenu as coption

import model
import proj
import param1
import param2
import layer

import context

class Root(tk.Frame, ga.GUIAbstract):
    defaultparam = context.root_default
    exampleparam = context.root_example
    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        ga.GUIAbstract.__init__(self, defaultparam=self.defaultparam)

        # [proj]    [model]
        # [    layer      ]
        # [param1] [param2]

        prow = 0

        # projectile
        self.projframe = tk.LabelFrame(self, text='Projectile')
        self.proj = proj.Proj(self.projframe)
        self.add_widget('proj', self.proj)
        self.proj.pack()
        self.projframe.grid(row=prow, column=0, columnspan=1)

        # model
        self.model = model.Model(self)
        self.add_widget('model', self.model)
        self.model.grid(row=prow, column=1, padx=(20,0), columnspan=1)
        prow += 1

        # layer
        self.layerframe = tk.LabelFrame(self, text='Target')
        self.layer = layer.Layer(self.layerframe)
        self.add_widget('layer', self.layer)
        self.layer.pack()

        self.layerframe.grid(row=prow, column=0, columnspan=2, sticky=tk.W+tk.E)
        prow += 1

        # buttom parameter frame
        self.paramframe = tk.Frame(self)
        # parameter1
        self.param1 = param1.Param1(self.paramframe)
        self.add_widget('param1', self.param1)
        self.param1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W, padx=5)

        # parameter2
        self.param2 = param2.Param2(self.paramframe)
        self.add_widget('param2', self.param2)
        self.param2.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W, padx=5)

        self.paramframe.grid(row=prow, column=0, columnspan=2, pady=5)

        self.clear()

if __name__ == '__main__':
    import tktool.gui_testframe as gt
    app = tk.Tk()

    gt.gui_testframe(app, Root, Root.exampleparam)

    app.mainloop()
