import Tkinter as tk

import tkFileDialog

class _Base(tk.Frame):
    _askaction = None
    def __init__(self, master=None, label='', textvariable=None, *args, **kw):
        """
        @textvariable path contents, None or tk.StringVar object
        """
        tk.Frame.__init__(self, master)
        self.label = label
        self.textvariable = textvariable

        if self.textvariable is None:
            self.textvariable = tk.StringVar()

        self.filepath = tk.Entry(self, textvariable=self.textvariable)
        self.btn = tk.Button(self, text='..', command=self.selectfilepath)

        self.filepath.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.btn.pack(side=tk.LEFT)

    def selectfilepath(self):
        #fname = tkFileDialog.asksaveasfilename(title=self.label,
        #        filetypes=[('All', '*')])
        fname = self._askaction(title=self.label, initialfile=self.textvariable.get(), filetypes=[('All', '*')])
        if fname:
            self.textvariable.set(fname)

    def set(self, v):
        self.textvariable.set(v)

    def get(self):
        return self.textvariable.get()

    def clear(self):
        self.textvariable.set('')

    def validate(self):
        return None

class Saveas(_Base):
    _askaction = staticmethod(tkFileDialog.asksaveasfilename)

class Open(_Base):
    _askaction = staticmethod(tkFileDialog.askopenfilename)
