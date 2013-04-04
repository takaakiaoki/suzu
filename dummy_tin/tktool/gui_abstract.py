import Tkinter as tk

class GUIAbstract(object):
    """common interface of gui. This is only reference for 
    gui classes it is not needed to be inherited.
    """

    def __init__(self, defaultparam={}):
        self.widgets = {}
        self.disabled = False
        self.defaultparam = defaultparam

    def add_widget(self, key, widget):
        self.widgets[key] = widget

    def clear(self):
        self.set({})

    def set(self, d):
        """set widget value
        @param args
        """
        for k, w in self.widgets.iteritems():
            w.set(d.get(k, self.defaultparam[k]))

    def get(self):
        """get widget value. get() does not validate the widget value,
        so it is recommended to call validate() before.
        if widget[k] is disabled, widget[k].get() is skipped.
        @return  widget value
        """
        d = {}
        for k, v in self.widgets.iteritems():
            if not v.is_disabled():
                d[k] = v.get()
        return d

    def get_nostatechk(self):
        """get widget value independent of the state of the widget"""
        d = {}
        for k, v in self.widgets.iteritems():
            d[k] = v.get_nostatechk()
        return d


    def validate(self):
        """validate widget value,
        It is recommended to change the widget property according to the
        validation result of widget value.
        @return None or (error structure), error can be parsed by error.py
        """
        if self.disabled:
            return None

        err = []
        for k, v in self.widgets.iteritems():
            r = v.validate()
            if r:
                err.append((k, r))

        return err if err else None

    def enable(self):
        for v in self.widgets.values():
            v.enable()
        self.disabled = False
        
    def disable(self):
        for v in self.widgets.values():
            v.disable()
        self.disabled = False

    def is_disabled(self):
        return self.disabled

class TunedEntry(tk.Entry):
    """arranged tk.Entry class to satisfy GUIAbstract convension"""
    def __init__(self, master=None, *args, **kw):
        tk.Entry.__init__(self, master, *args, **kw)

        if 'textvariable' not in kw:
            if 'Varclass' in kw:
                self.cv = kw['Varclass'](self)
                del kw['Varclass']
            else:
                self.cv = tk.StringVar(self)
            kw['textvariable'] = self.cv
        else:
            self.cv = kw['textvariable']

        self.config(textvariable=self.cv)

    def set(self, d):
        self.cv.set(d)

    def get(self):
        if self.is_disabled():
            return None
        return self.cv.get()

    def get_nostatechk(self):
        return self.cv.get()

    def validate(self):
        if self.is_disabled():
            return None

        err = None
        try:
            v = self.cv.get()
        except Exception as e:
            err = str(e)

        return err

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED
