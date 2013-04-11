import sys
import json
import os.path
import subprocess

import Tkinter as tk
import tkFileDialog
import tkMessageBox

import tktool.error

import root as _root
import to_trim

import context
import profile

profile_pathinfo = None
profile_config = None

def spawn_trim(trim_in_path):
    """spawn trim.exe"""
    fname = os.path.basename(trim_in_path)
    bname = os.path.dirname(trim_in_path)
    texename = os.path.join(bname, u'trim.exe')

    if fname.upper() == u'TRIM.IN' and os.path.exists(texename): 
        s = tkMessageBox.askyesno('Start TRIM?','You have updated TRIM.in file where TRIM.exe exists\n Will you start TRIM.exe calculation?')

        if s:
            # spawn trim.exe
            subprocess.Popen([texename], cwd=bname)


def run():
    # load profile data
    global profile_config
    global profile_pathinfo

    try:
        profile_pathinfo = profile.initialize()
        profile_config = profile.load_config(open(profile_pathinfo['config'],'r'))
    except profile.Error as e:
        tkMessageBox.showerror('error on loding profile data', 'error on loding profile data.\n\n'+ e)
        sys.exit(2)
    except Exception as e:
        tkMessageBox.showerror('error on loding profile data', 'error on loding profile data.\n\n'+ str(e))
        sys.exit(2)

    app = tk.Tk()
    # setup gui

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
        global profile_pathinfo
        global profile_config
        fname = tkFileDialog.askopenfilename(title=u'Load json file',
                defaultextension='.json', initialfile='TRIM.in.json',
                initialdir=profile_config['lastdir'],
                filetypes=[('JSON', '*.json'), ('All', '*')])
        if fname:
            with open(fname, 'rt') as stream:
                # save as json format
                d = json.load(stream)
                # check version of json data and solve it
                d = context.solve_version(d)
                root.set(d)

                # load successed save lastdir
                profile_config['lastdir'] = os.path.dirname(fname)
                profile.dump_config(profile_config,
                        open(profile_pathinfo['config'], 'w'))

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

        global profile_pathinfo
        global profile_config

        fname = tkFileDialog.asksaveasfilename(
                title=u'Save TRIM input file',
                initialfile='TRIM.in',
                initialdir=profile_config['lastdir'],
                filetypes=[('TRIM input', '*.in'), ('All', '*')])
        if fname:
            # add context version
            d['version'] = context.currentversion

            # 0. remove existing .json
            json_name = fname + u'.json'
            if os.path.exists(json_name):
                os.unlink(json_name)

            # 1. dump .json.temp
            jsont_name = fname + u'.json.t'
            with open(jsont_name, 'wt') as stream: 
                json.dump(d, stream, indent=2, sort_keys=True)

            # 2. save as trim data format 
            with open(fname, 'wt') as stream:
                to_trim.to_trim(d, stream)

            # 3. rename .json.temp to .json 
            os.rename(jsont_name, json_name)

            # file dump succeeded, save lastdir in the profile
            profile_config['lastdir'] = os.path.dirname(fname)
            profile.dump_config(profile_config,
                    open(profile_pathinfo['config'],'w'))

            spawn_trim(fname)

    getandsavebtn = tk.Button(menuframe, text='Save (& run TRIM)', command=save_action)
    getandsavebtn.grid(row=0, column=pcol, padx=5)

    menuframe.pack(side=tk.TOP)

    app.mainloop()
