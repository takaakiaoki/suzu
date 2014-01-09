import Tkinter as tk
import tkSimpleDialog

class MatDB(tkSimpleDialog.Dialog):
    def __init__(self, parent, opts, title=None):
        self.result = None
        self.opts = opts
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        # create scrolled listbox
        listframe = tk.Frame(master, bd=2, relief=tk.SUNKEN)

        self.scrlistbox = tk.Scrollbar(listframe)
        self.scrlistbox.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(listframe, bd=0, yscrollcommand=self.scrlistbox.set)
        self.listbox.pack()
        
        self.scrlistbox.config(command=self.listbox.yview)

        self.listbox.config(width=20)
        self.listbox.insert(tk.END, *[a['name'] for a in self.opts])
        self.listbox.bind('<<ListboxSelect>>', self.lbselect)

        listframe.grid(row=0, column=0)

        self.summary = tk.Text(master)
        self.summary.insert(tk.END, 'not selected')
        self.summary.config(state=tk.DISABLED)

        self.summary.config(height=20, width=40, wrap=tk.WORD)
        self.summary.grid(row=0, column=1)

    def lbselect(self, evt):
        idx = int(self.listbox.curselection()[0])
        self.summary.config(state=tk.NORMAL)
        self.summary.delete(1.0, tk.END)
        self.summary.insert(tk.END, self.opts[idx]['summary'])
        self.summary.config(state=tk.DISABLED)

    def apply(self):
        i = self.listbox.curselection()
        self.result = i

if __name__ == '__main__':
    app = tk.Tk()

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
            {'name':"N", 'summary':'summary of N'}]

    # test for less entries
    # del(opts[3:])

    d = MatDB(app, entries)

    # print type(d)
    # print d.__dict__
    print d.result
