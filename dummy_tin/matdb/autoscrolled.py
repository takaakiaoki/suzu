import Tkinter as tk

class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    # taken from http://effbot.org/zone/tkinter-autoscrollbar.htm
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            #self.tk.call("grid", "remove", self)
            self.grid_remove()
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"

class AutoScrolledText(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)

        self._vscrollbar = AutoScrollbar(self)
        self._hscrollbar = AutoScrollbar(self, orient=tk.HORIZONTAL)
        self._text = tk.Text(self,
                yscrollcommand=self._vscrollbar.set,
                xscrollcommand=self._hscrollbar.set)

        self._text.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self._vscrollbar.config(command=self._text.yview)
        self._hscrollbar.config(command=self._text.xview)

        self._vscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        self._hscrollbar.grid(row=1, column=0, sticky=tk.E+tk.W)

        # make the canvas expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def text_config(self, *arg, **kw):
        return self._text.config(*arg, **kw)

    def text_insert(self, *arg, **kw):
        return self._text.insert(*arg, **kw)

    def text_delete(self, *arg, **kw):
        return self._text.delete(*arg, **kw)

