import tkinter as tk
import tkinter.filedialog

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
        #fname = tkinter.filedialog.asksaveasfilename(title=self.label,
        #        filetypes=[('All', '*')])
        oldpath = self.textvariable.get()
        newpath = self._askaction(title=self.label, initialfile=oldpath,
                filetypes=[('All', '*')])
        if newpath:
            self.on_fileselected(newpath, oldpath)

    def on_fileselected_default(self, newpath, oldpath):
        self.textvariable.set(newpath)

    # customized action when selectfilepath choosed collect filepath
    on_fileselected = on_fileselected_default

    def set(self, v):
        self.textvariable.set(v)

    def get(self):
        return self.textvariable.get()

    def clear(self):
        self.textvariable.set('')

    def validate(self):
        return None

class Saveas(_Base):
    _askaction = staticmethod(tkinter.filedialog.asksaveasfilename)

class Open(_Base):
    _askaction = staticmethod(tkinter.filedialog.askopenfilename)
