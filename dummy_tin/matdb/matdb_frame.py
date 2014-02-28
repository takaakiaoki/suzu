import Tix as tix

def _hlist_path_walk(hlist, root='', topdown=True):
    """pick-up all path entries in HList is the same manner as os.walk
    """
    dirs = []
    files = []
    for e in hlist.info_children(root):
        if hlist.info_children(e):
            dirs.append(e)
        else:
            files.append(e)
    if topdown:
        # topdown order
        yield root, dirs, files
        for d in dirs:
            for e in _hlist_path_walk(hlist, d, topdown):
                yield e
    else:
        # bottomup order
        for d in dirs:
            for e in _hlist_path_walk(hlist, d, topdown):
                yield e
        yield root, dirs, files

class MatDBFrame(tix.Frame):
    def __init__(self, parent, opts, title=None):
        tix.Frame.__init__(self, parent, title)

        self.opts = opts
        self.pathmap = {} # (path in listbox) -> (element of opts)
        
        self.pwindow = tix.PanedWindow(self, orientation='horizontal')

        self.p1 = self.pwindow.add('p1', at=0, expand=0)
        self.p2 = self.pwindow.add('p2', at=1, expand=1)

        # create scrolled listbox
        listframe = tix.Frame(self.p1, bd=2, relief=tix.SUNKEN)

        self.listbox = tix.Tree(listframe, browsecmd=self._browsecommand)
        self.listbox.hlist.config(width=40)
        self.listbox.pack(expand=True, fill=tix.BOTH)
        self._set_listbox_entries(self.opts)

        # self.listbox.insert(tix.END, *[a['name'] for a in self.opts])
        # self.listbox.bind('<<ListboxSelect>>', self._lbselect)

        listframe.grid_rowconfigure(0, weight=1)
        listframe.grid_columnconfigure(0, weight=1)

        listframe.grid(row=0, column=0, padx=(0,5), sticky=tix.N+tix.S+tix.E+tix.W)
        self.p1.rowconfigure(0,weight=1)
        self.p1.columnconfigure(0,weight=1)

        # for some version of tix, auto option does not work but acts like 'both'
        self.summary = tix.ScrolledText(self.p2, bd=2, scrollbar='auto', relief=tix.SUNKEN)

        self.summary.text.config(width=80)
        self.summary.text.config(wrap=tix.NONE)
        self._set_summary_text('not selected')

        self.summary.grid(row=0, column=0, padx=(5,0), sticky=tix.N+tix.S+tix.E+tix.W)
        self.p2.rowconfigure(0,weight=1)
        self.p2.columnconfigure(0,weight=1)

        self.pwindow.grid(row=0, column=0, sticky=tix.N+tix.S+tix.E+tix.W)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


    def _set_listbox_entries(self, entries):
        for e in entries:
            self.pathmap[e['path']] = e
            self.listbox.hlist.add(e['path'], itemtype=tix.TEXT, text=e['title'])
        # walk hlist hierarchy and close all paths
        for root, dirs, files in _hlist_path_walk(self.listbox.hlist, topdown=False):
            for d in dirs:
                self.listbox.setmode(d, 'close')
                self.listbox.close(d)

    def clear_listbox_entries(self):
        self.pathmap = {}
        self.listbox.hlist.clear()
        self._set_summary_text('not selected')

    def _set_summary_text(self, text):
        self.summary.text.config(state=tix.NORMAL)
        self.summary.text.delete(1.0, tix.END)
        self.summary.text.insert(tix.END, text)
        self.summary.text.config(state=tix.DISABLED)

    def _browsecommand(self, entry):
        self._set_summary_text(self.pathmap[entry]['summary'])

    def get_current_selection(self):
        v = self.listbox.hlist.info_selection()
        if v:
            return self.pathmap[v[0]].get('content', None)
        return None

# demostration is found at demos/demo_matdb_frame.py
