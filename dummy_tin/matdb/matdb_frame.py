import Tix as tix

import autoscrolled

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
            self.listbox.hlist.add(e['path'], itemtype=tix.TEXT, text=e['path'])

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
            return self.pathmap[v[0]]
        return None

if __name__ == '__main__':
    app = tix.Tk()

    entries = [{'path':"A", 'summary':'summary of A'},
            {'path':"B", 'summary':'summary of B'},
            {'path':"C", 'summary':'summary of C'},
            {'path':"D", 'summary':'summary of D'},
            {'path':"E", 'summary':'summary of E'},
            {'path':"F", 'summary':'summary of F'},
            {'path':"G", 'summary':'summary of G'},
            {'path':"H", 'summary':'summary of H'},
            {'path':"I", 'summary':'summary of I'},
            {'path':"J", 'summary':'summary of J'},
            {'path':"K", 'summary':'summary of K'},
            {'path':"L", 'summary':'summary of L'},
            {'path':"M", 'summary':'summary of M'},
            {'path':"N", 'summary':
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
a''' }]

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
