import Tix as tix
import os

import matdb_frame

class Dialog(tix.Toplevel):

    def __init__(self, parent, opts, title = None):

        tix.Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.initial_focus = None
        self.bodyframe = matdb_frame.MatDBFrame(self, opts)

        self.bodyframe.grid(row=0, column=0, sticky=tix.N+tix.S+tix.E+tix.W)

        self.buttonframe = tix.Frame(self)
        self.buttonbox(self.buttonframe)
        self.buttonframe.grid(row=1, column=0, sticky=tix.N+tix.S)

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.initial_focus.focus_set()

    #
    # construction hooks
    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        pass

    def buttonbox(self, master):
        # add standard button box. override if you don't want the
        # standard buttons

        w = tix.Button(master, text="OK", width=10, command=self.ok, default=tix.ACTIVE)
        w.pack(side=tix.LEFT, padx=5, pady=5)
        w = tix.Button(master, text="Cancel", width=10, command=self.cancel)
        w.pack(side=tix.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

    #
    # standard button semantics
    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks
    def validate(self):
        return 1 # override

    def apply(self):
        self.result = self.bodyframe.get_current_selection()
