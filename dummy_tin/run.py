import json
import os.path

import Tkinter as tk
import tkFileDialog
import tkMessageBox

import tktool.error

import root as _root
import to_trim

lastdir = ''

def run():
    app = tk.Tk()

    root = _root.Root(app)

    root.pack(side=tk.TOP)

    menuframe = tk.Frame(app)

    pcol = 0

    def set_action():
        root.set(_root.Root.exampleparam)

    setbtn = tk.Button(menuframe, text='Set Example', command=set_action)
    setbtn.grid(row=0, column=pcol, padx=5)
    pcol += 1

    def clear_action():
        root.clear()

    clearbtn = tk.Button(menuframe, text='Clear', command=clear_action)
    clearbtn.grid(row=0, column=pcol, padx=5)
    pcol += 1

    # get data and display on console
    def get_action():
        print root.get()
    getbtn = tk.Button(menuframe, text='Dump to Console', command=get_action)
    getbtn.grid(row=0, column=pcol, padx=5)
    pcol += 1

    def val_action():
        err = root.validate()
        if err:
            tktool.error.show_as_messagebox(err)

    valbtn = tk.Button(menuframe, text='Validate', command=val_action)
    valbtn.grid(row=0, column=pcol, padx=5)
    pcol += 1

    def load_action():
        global lastdir
        fname = tkFileDialog.askopenfilename(title=u'Load json file', defaultextension='.json', initialfile='TRIM.in.json', initialdir=lastdir, filetypes=[('JSON', '*.json'), ('All', '*')])
        if fname:
            with open(fname, 'rt') as stream:
                # save as json format
                d = json.load(stream)
                root.set(d)
                # save lastdir
                lastdir = os.path.dirname(fname)

    loadbtn = tk.Button(menuframe, text='Load .json', command=load_action)
    loadbtn.grid(row=0, column=pcol, padx=5)
    pcol += 1


    def save_action():
        class VExecption(Exception):
            def __init__(self, err):
                Exception.__init__(self)
                self.err = err

        try:
            err = root.validate()
            if err:
                raise VExecption(err)
            d = root.get()
        except VExecption as e:
            tkMessageBox.showerror('Validation error', 'validation error, save is aborted.\n\n'+tktool.error.format_errorstruct(e.err))
            return
        except Error as e:
            tkMessageBox.showerror('exception error', 'exception received, save is aborted.\n'+e)
            return

        global lastdir

        fname = tkFileDialog.asksaveasfilename(title=u'Save marlowe (&json) control file', initialfile='TRIM.in', initialdir=lastdir, filetypes=[('TRIM input', '*.in'), ('All', '*')])
        if fname:
            # save as marlowe format 
            stream = open(fname, 'wt')
            to_trim.to_trim(d, stream)
            # save as json format
            stream = open(fname+u'.json', 'wt')
            json.dump(d, stream, indent=4, sort_keys=True)

            lastdir = os.path.dirname(fname)

    getandsavebtn = tk.Button(menuframe, text='Save', command=save_action)
    getandsavebtn.grid(row=0, column=pcol, padx=5)

    menuframe.pack(side=tk.TOP)

    app.mainloop()
