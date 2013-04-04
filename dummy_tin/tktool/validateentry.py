"""gui entry box with data validation
    .validate(): validate control data
        if validation error ocuurs, entry box is truned red. If the entry box is safe, it is turned white.
        this function returns (stat, reason), where,
        stat is validation result (True or False)
        reason is structured error messeage which would be parsed by error.walk_errorstruct()

    .get() return control variables. it may cause exception.
    it would be recommended to run .validate() befor get()
"""

import Tkinter as tk

class ValidateAbstract(object):
    def validate(self):
        """validate control value
        @return errorstruct defined at error.py
        """
        return None



class Int(tk.Entry):
    def __init__(self, master, textvariable=None, cnf={}, **kw):
        """
        @param textvariable Tkinter.IntVar object watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, cnf, bg='white', **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.IntVar(master)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return reason

        try:
            tmp = self.cv.get()
        except ValueError:
            reason = 'ValueError (should be Int)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')
        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED



class Double(tk.Entry):
    def __init__(self, master=None, textvariable=None, *args, **kw):
        """
        @param textvariable Tkinter.DoubleVar value watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, bg='white', *args, **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.DoubleVar(self)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return None
        try:
            v = self.cv.get()
        except ValueError:
            reason = 'ValueError (should be Double)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')
        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED



class IntPositive(tk.Entry):
    def __init__(self, master, textvariable=None, cnf={}, **kw):
        """
        @param textvariable Tkinter.IntVar object watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, cnf, bg='white', **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.IntVar(master, 1)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return None
        try:
            tmp = self.cv.get()
            if tmp <= 0:
                reason = 'int value is not positive'
        except ValueError:
            reason = 'ValueError (should be Int)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')
        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED

class IntZeroPositive(tk.Entry):
    def __init__(self, master, textvariable=None, cnf={}, **kw):
        """
        @param textvariable Tkinter.IntVar object watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, cnf, bg='white', **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.IntVar(master, 1)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return None
        try:
            tmp = self.cv.get()
            if tmp < 0:
                reason = 'int value is not zero or positive'
        except ValueError:
            reason = 'ValueError (should be Int)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')
        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED

class DoublePositive(tk.Entry):
    def __init__(self, master, textvariable=None, cnf={}, **kw):
        """
        @param textvariable Tkinter.IntVar object watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, cnf, bg='white', **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.DoubleVar(master, 1.0)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return reason

        try:
            tmp = self.cv.get()
            if tmp <= 0:
                reason = 'double value is not positive'
        except ValueError:
            reason = 'ValueError (should be Double)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')

        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED


class DoubleZeroPositive(tk.Entry):
    def __init__(self, master, textvariable=None, cnf={}, **kw):
        """
        @param textvariable Tkinter.IntVar object watched by this widget.
               If not given, variable object is generate inside the class.
        """
        tk.Entry.__init__(self, master, cnf, bg='white', **kw)
        if textvariable:
            self.cv = textvariable
        else:
            self.cv = tk.DoubleVar(master, 1.0)
        self.config(textvariable=self.cv)

    def set(self, v):
        self.cv.set(v)

    def get(self):
        return self.cv.get()

    def get_nostatechk(self):
        return self.get()

    def validate(self):
        reason = None
        if self.is_disabled():
            return reason

        try:
            tmp = self.cv.get()
            if tmp < 0.0:
                reason = 'double value is not zero or positive'
        except ValueError:
            reason = 'ValueError (should be Double)'

        if reason:
            self.config(bg='red')
        else:
            self.config(bg='white')

        return reason

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED


def VecNdFactory(Base_, dim_):
    """factory class for N-dim double vector
        @param Base base widget class such like Int or Double defined above
        @param dim array dimension
    """
    class V(tk.Frame):
        Base = Base_
        dim = dim_

        def __init__(self, master=None, textvariable=None, *args, **kw):
            """
            @param textvariable
              [type(Base.cv)]*dim value watched by this widget.
              If not given, variable object is generate inside the class.
            """
            tk.Frame.__init__(self, master)

            self.disabled = False

            if textvariable:
                self.array = [self.Base(self, textvariable=t) for t in textvariable[:self.dim]]
            else:
                self.array = [self.Base(self) for i in range(self.dim)]

            for a in self.array:
                a.pack(side=tk.LEFT)

        def config(self, **kw):
            """apply configuration for all widgets
            """
            for a in self.array:
                a.config(**kw)

        def set(self, val):
            for a, v in zip(self.array, val):
                a.set(v)

        def get(self):
            v = []
            for a in self.array:
                if not a.is_disabled():
                    v.append(a.get())
                else:
                    v.append(None)
            return v

        def get_nostatechk(self):
            v = []
            for a in self.array:
                v.append(a.get_nostatechk())
            return v

        def validate(self):
            if self.is_disabled():
                return None

            err = []
            for idx, widget in enumerate(self.array):
                r = widget.validate()
                if r:
                    err.append(('[{0:d}]'.format(idx), r))
                    
            return err if err else None

        def enable(self):
            for a in self.array:
                a.config(state=tk.NORMAL)
            self.disabled = False


        def disable(self):
            for a in self.array:
                a.config(state=tk.DISABLED)
            self.disabled = True

        def is_disabled(self):
            return self.disabled


    return V

Vec2Int = VecNdFactory(Int, 2)
Vec3Int = VecNdFactory(Int, 3)
Vec3IntPositive = VecNdFactory(IntPositive, 3)
Vec2d = VecNdFactory(Double, 2)
Vec3d = VecNdFactory(Double, 3)
Vec4d = VecNdFactory(Double, 4)
