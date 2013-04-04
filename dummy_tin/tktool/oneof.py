# oneof --  gui class to represent array of large widget
#   

import Tkinter as tk

import tkMessageBox

import copy

import validateentry
import codedoptionmenu
import error

def OneofFactory(GUIElem, defaultelem):
    """genelates one-of class which represents array of GUIElem
    @param GUIElem gui class implemented with 
    @param defaultelem default value to initialize GUIElem
    """
    class C(tk.Frame):
        class Error(Exception):
            def __init__(self, err):
                Exception.__init__(self)
                self.err = err

        def __init__(self, master=None, *args, **kw):
            tk.Frame.__init__(self, master)

            self.elemdata = []
            self.currentview = None # index number for elemdata which
                                    # elemdata is shown on self.view

            prow = 0

            # index it returns None when elemdata is null
            # or (0, 1, 2, ...) when elemdata has member
            self.indexoption = [(None, '--')]
            self.index = codedoptionmenu.CodedOptionMenu(self,
                    self.indexoption)

            self.index.config(width=3)
            self.index.grid(row=prow, rowspan=2, column=0, sticky=tk.E)

            # number of elems
            self.totallabel = tk.Label(self,
                    text='of {0:d}'.format(len(self.elemdata)))
            self.totallabel.grid(row=prow, rowspan=2, column=1, sticky=tk.W)

            # add elem in the tail
            self.append = tk.Button(self, text='add (& move) to last',
                    command=self.append_action)
            self.append.grid(row=prow, column=2, sticky=tk.W)

            # delete current view
            self.delete = tk.Button(self, text='delete this view',
                    command=self.delete_action)
            self.delete.grid(row=prow+1, column=2, sticky=tk.W)
            prow += 2

            # view
            self.view = GUIElem(self)
            self.view.grid(row=prow, column=0, columnspan=3)
            prow += 1

            self.disabled = False

            self.clear()

        def store_currentview(self):
            """store widget data to self.elemdata[self.currentview].
            self.view is validated and may cause exception.
            """
            if self.currentview is not None:
                e = self.view.validate()
                if e:
                    raise self.Error(e)
                self.elemdata[self.currentview] = self.view.get()

        def show_currentview(self):
            if self.currentview is None:
                self.view.disable()
            else:
                self.view.enable()
                self.view.set(self.elemdata[self.currentview])
                # view is validated in order to clear previous validation error
                self.view.validate()
            self.index.set(self.currentview)

        def index_action(self, value):
            """action when self.index is changed
            this function is bound with self.index, so that 'value' argument is passed
            """
            # firstly, store context shown at self.view
            # validation might be required but not yet
            try:
                self.store_currentview()
            except self.Error as e:
                # validation error, do not move index and exit
                self.index.set(self.currentview)
                tkMessageBox.showerror('Validation error', 'validation error '+error.format_errorstruct(e.err))
                return 
            
            # then load new elem data and show it
            # self.index returns None or 0, 1, 2 ...
            self.currentview = self.index.get()

            self.show_currentview()

        def update_menuoption(self):
            # update indexoption, and tatallabel
            if len(self.elemdata):
                self.indexoption = [(i, str(i+1)) for i in range(len(self.elemdata))]
            else:
                self.indexoption = [(None, '--')]

            self.index.set_new_option(self.indexoption, command=self.index_action)

            self.totallabel.config(text='of {0:d}'.format(len(self.elemdata)))

        def append_action(self):
            # store current view
            try:
                self.store_currentview()
            except self.Error as e:
                # validation error, do not append element
                tkMessageBox.showerror('Validation error', 'validation error '+error.format_errorstruct(e.err))
                return 

            # add default element
            self.elemdata.append(copy.deepcopy(defaultelem))
            self.update_menuoption()
            # view newly added elem
            self.currentview = len(self.elemdata) - 1
            self.show_currentview()

        def delete_action(self):
            """delete element on self.currentview"""
            if self.currentview is None:
                # nothing to do
                return
            del(self.elemdata[self.currentview])
            self.update_menuoption()
            # what is the next currentview?
            self.currentview = min(self.currentview, len(self.elemdata)-1)
            if self.currentview == -1:
                self.currentview = None
            self.show_currentview()

        def set(self, d):
            self.elemdata = copy.deepcopy(d)

            # update option
            self.update_menuoption()

            # set menuoption
            if len(self.elemdata):
                self.currentview = 0
            else:
                self.currentview = None
            self.show_currentview()

        def get(self):
            if self.is_disabled():
                return None
            # store current view 
            self.store_currentview()
            d = copy.deepcopy(self.elemdata)
            return d

        def get_nostatechk(self):
            # store current view 
            self.store_currentview()
            d = copy.deepcopy(self.elemdata)
            return d

        def clear(self):
            # first fill view with default
            self.view.set(defaultelem)
            # and cleare truly
            self.set([])

        def validate(self):
            if self.is_disabled():
                return None
            return self.view.validate()

        def enable(self):
            self.index.config(state=tk.NORMAL)
            self.append.config(state=tk.NORMAL)
            self.delete.config(state=tk.NORMAL)
            if len(self.elemdata):
                self.view.enable()
            self.disabled = False

        def disable(self):
            self.index.config(state=tk.DISABLED)
            self.append.config(state=tk.DISABLED)
            self.delete.config(state=tk.DISABLED)
            self.view.disable()
            self.disabled = True

        def is_disabled(self):
            return self.disabled

    return C


if __name__ == '__main__':
    app = tk.Tk()

    # element class
    class Elem(tk.Frame):
        def __init__(self, master=None, *args, **kw):
            tk.Frame.__init__(self, master)

            self.w = validateentry.Double(self)

            self.w.pack()

            self.clear()

        def set(self, d):
            self.w.set(d)

        def get(self):
            return self.w.get()

        def clear(self):
            self.set(0)

        def validate(self):
            return self.w.validate()

        def enable(self):
            self.w.config(state=tk.NORMAL)

        def disable(self):
            self.w.config(state=tk.DISABLED)


    C = OneOfFactory(Elem, 1)

    gui = C(app)
    gui.pack(side=tk.TOP)

    # test buttons
    testframe = tk.Frame(app)
    # set default
    def set_action():
        gui.set([1, 2, 3, 4, 5, 6])
    setbtn = tk.Button(testframe, text='set example', command=set_action)
    setbtn.pack(side=tk.LEFT, pady=2)
    # get
    def get_action():
        print gui.get()
    getbtn = tk.Button(testframe, text='get', command=get_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # clear
    def clear_action():
        gui.clear()
    clearbtn = tk.Button(testframe, text='clear', command=clear_action)
    clearbtn.pack(side=tk.LEFT, pady=2)
    # validate
    def validate_action():
        print gui.validate()
    getbtn = tk.Button(testframe, text='validate', command=validate_action)
    getbtn.pack(side=tk.LEFT, pady=2)

    # enable
    def enable_action():
        gui.enable()
    enablebtn = tk.Button(testframe, text='enable', command=enable_action)
    enablebtn.pack(side=tk.LEFT, pady=2)

    # disable
    def disable_action():
        gui.disable()
    disablebtn = tk.Button(testframe, text='disable', command=disable_action)
    disablebtn.pack(side=tk.LEFT, pady=2)

    testframe.pack(side=tk.TOP)

    app.mainloop()
