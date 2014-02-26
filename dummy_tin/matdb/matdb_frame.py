import Tix as tix

import autoscrolled

class MatDBFrame(tix.Frame):
    def __init__(self, parent, opts, title=None):
        tix.Frame.__init__(self, parent, title)

        self.opts = opts

        # create scrolled listbox
        listframe = tix.Frame(self, bd=2, relief=tix.SUNKEN)

        self.scrlistbox = autoscrolled.AutoScrollbar(listframe)
        self.scrlistbox.grid(row=0, column=1, sticky=tix.N+tix.S)

        self.listbox = tix.Listbox(listframe, bd=0, yscrollcommand=self.scrlistbox.set)
        self.listbox.grid(row=0, column=0, sticky=tix.N+tix.E+tix.S+tix.W)
        self.scrlistbox.config(command=self.listbox.yview)

        self.listbox.config(width=20)
        self.listbox.insert(tix.END, *[a['name'] for a in self.opts])
        self.listbox.bind('<<ListboxSelect>>', self._lbselect)

        listframe.grid_rowconfigure(0, weight=1)
        listframe.grid_columnconfigure(0, weight=1)
        listframe.grid(row=0, column=0, sticky=tix.N+tix.S+tix.E+tix.W)

        # for some version of tix, auto option does not work but acts like 'both'
        self.summary = tix.ScrolledText(self, bd=2, scrollbar='auto', relief=tix.SUNKEN)

        self.summary.text.config(width=60)
        self.summary.text.insert(tix.END, 'not selected')
        self.summary.text.config(state=tix.DISABLED, wrap=tix.NONE)

        self.summary.grid(row=0, column=1, sticky=tix.N+tix.S+tix.E+tix.W)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

    def _lbselect(self, evt):
        idx = int(self.listbox.curselection()[0])
        self.summary.text.config(state=tix.NORMAL)
        self.summary.text.delete(1.0, tix.END)
        self.summary.text.insert(tix.END, self.opts[idx]['summary'])
        self.summary.text.config(state=tix.DISABLED)
        # self.summary.update_idletasks()

    def get_current_selection(self):
        v = self.listbox.curselection()
        if v:
            # list is selected. return number of selected item
            return v[0]
        return 0 # 0 means no item is selected

if __name__ == '__main__':
    app = tix.Tk()

    entries = [{'name':"A", 'summary':'summary of A'},
            {'name':"B", 'summary':'summary of B'},
            {'name':"C", 'summary':'summary of C'},
            {'name':"D", 'summary':'summary of D'},
            {'name':"E", 'summary':'summary of E'},
            {'name':"F", 'summary':'summary of F'},
            {'name':"G", 'summary':'summary of G'},
            {'name':"H", 'summary':'summary of H'},
            {'name':"I", 'summary':'summary of I'},
            {'name':"J", 'summary':'summary of J'},
            {'name':"K", 'summary':'summary of K'},
            {'name':"L", 'summary':'summary of L'},
            {'name':"M", 'summary':'summary of M'},
            {'name':"N", 'summary':
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
