import Tix as tix

def hlist_path_walk(hlist, root='', topdown=True):
    """pick-up all path entries in HList is the same manner as os.walk
    """
    dirs = []
    files = []
    for e in hlist.info_children(root):
        if hlist.info_children(e):
            dirs.append(e)
        else:
            files.append(e)
    # topelevel order
    if topdown:
        yield root, dirs, files
        for d in dirs:
            for e in hlist_path_walk(hlist, d, topdown):
                yield e
    else:
        for d in dirs:
            for e in hlist_path_walk(hlist, d, topdown):
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
        self.listbox.hlist.config(width=20)
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

        self.summary.text.config(width=60)
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
        for root, dirs, files in hlist_path_walk(self.listbox.hlist, topdown=False):
            for d in dirs:
                self.listbox.setmode(d, 'close')
                self.listbox.close(d)

    def _set_summary_text(self, text):
        self.summary.text.config(state=tix.NORMAL)
        self.summary.text.delete(1.0, tix.END)
        self.summary.text.insert(tix.END, text)
        self.summary.text.config(state=tix.DISABLED)


    def _browsecommand(self, entry):
        self._set_summary_text(self.pathmap[entry]['summary'])

    #def _lbselect(self, evt):
    #    idx = int(self.listbox.curselection()[0])
    #    self._set_summary_text(self.opts[idx]['summary'])

    def get_current_selection(self):
        v = self.listbox.hlist.info_selection()
        if v:
            return self.pathmap[v[0]].get('content', None)
        return None

if __name__ == '__main__':
    app = tix.Tk()

    # entries
    # {'path':, 'path of Hlist seperated with '.'}
    #   'title': string shown at listbox
    #   'summary': texts shown in summary field
    #   'content': (optional) value to be returend
    #              (None is allowed, and applied for directory entry for example)
    #}
    entries = [
        {'path':"A", 'title':'A', 'summary':'Directory A'},
        {'path':"A.B", 'title':'B', 'summary':'summary of B', 'content':11},
        {'path':"A.C", 'title':'C', 'summary':'summary of C', 'content':12},
        {'path':"A.D", 'title':'D', 'summary':'summary of D', 'content':13},
        {'path':"A.E", 'title':'E', 'summary':'summary of E', 'content':14},
        {'path':"F", 'title':'F', 'summary':'Directory F'},
        {'path':"F.G", 'title':'G', 'summary':'summary of G', 'content':21},
        {'path':"F.H", 'title':'H', 'summary':'summary of H', 'content':22},
        {'path':"F.I", 'title':'I', 'summary':'Directory F.I'},
        {'path':"F.I.J", 'title':'J', 'summary':'summary of J', 'content':231},
        {'path':"F.I.K", 'title':'K', 'summary':'summary of K', 'content':232},
        {'path':"L", 'title':'L', 'summary':'Directory L'},
        {'path':"L.M", 'title':'M', 'summary':'summary of M', 'content':31},
        {'path':"L.N", 'title':'N', 'summary':
            '''\
summary of N
very very very long long long long summary
0
1
2
3
4
5
6
:
a''', 'content':32}]

    # test for less entries
    #del(entries[3:])

    top = tix.Toplevel()
    d = MatDBFrame(top, entries)
    d.grid(row=0, column=0, sticky=tix.N+tix.E+tix.S+tix.W)
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    def c():
        print d.get_current_selection()

    tix.Button(app, text='get value', command=c).pack()

    top.wait_window()

    app.mainloop()

    # print type(d)
    # print d.__dict__
