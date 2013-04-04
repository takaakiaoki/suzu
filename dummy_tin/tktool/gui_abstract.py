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
