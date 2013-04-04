import Tkinter as tk

class TruncatedEntry(tk.Entry):
    """Entry which length is limitted
    """
    def __init__(self, master=None, limitwidth=None, *args, **kw):
        tk.Entry.__init__(self, master, bg='white', *args, **kw)
        self.limitwidth = limitwidth
        self.cv = tk.StringVar(self)
        # hack to hook .global(get|set)globalvar
        # see https://anuga.anu.edu.au/svn/anuga/branches/numpy/anuga/pmesh/PmwBlt.py
        if master:
            self._master = master
        else:
            self._master = tk._default_root
        self.tk = self._master.tk


        # generate text truncator
        # see
        #   http://effbot.org/tkinterbook/variable.htm
        #   http://www.astro.washington.edu/users/rowen/ROTKFolklore.html
        #   http://nsa.kpu-m.ac.jp/gijutu/python/man-gui/man-gui.php
        #   http://stackoverflow.com/questions/4140437/python-tkinter-interactively-validating-entry-widget-content  
        if self.limitwidth:
            def trace_truncate_text(name, index, mode):
                var = self.tk.globalgetvar(name)
                if len(var) > self.limitwidth:
                    # truncation
                    var = var[:self.limitwidth]
                    # writeback
                    self.tk.globalsetvar(name, var)
            self.cv.trace('w', trace_truncate_text)

        self.config(textvariable=self.cv)


    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def validate(self):
        stat, reason = True, None
        try:
            v = self.get()
        except ValueError:
            stat = False
            reason = 'ValueError occured in self.cv.get()'
        # check length of the text
        if self.limitwidth and len(v) > self.limitwidth:
            stat = False
            reason = 'text length is larger than limitation'

        if stat:
            self.config(bg='white')
        else:
            self.config(bg='red')
        return stat, reason


if __name__ == '__main__':
    app = tk.Tk()

    lentry = TruncatedEntry(app, limitwidth=10)
    lentry.pack()

    def val_lentry():
        print lentry.validate()

    def get_lentry():
        print lentry.get()

    btn_validate = tk.Button(app, text='validate', command=val_lentry)
    btn_validate.pack()

    btn_get = tk.Button(app, text='get', command=get_lentry)
    btn_get.pack()

    app.mainloop()
