import Tkinter as tk

import physics.element as elem
import db.disp as disp

import tktool
import tktool.validateentry
import context

maxatoms = 8

defaultparam_elem = context.atomtbl_elem_default

exampleparam = context.atomtbl_example

class AtomTbl(tk.Frame):
    def __init__(self, master=None, nsymbol=1, *args, **kw):
        tk.Frame.__init__(self, master)

        self.disabled = False

        prow = 0

        # number of valid atoms
        self.nsymbolfrm = tk.Frame(self)
        self.nsymbollabel = tk.Label(self.nsymbolfrm, text='size')
        self.nsymbolvar = tk.IntVar(self)

        self.nsymbol = tk.Spinbox(self.nsymbolfrm, textvariable=self.nsymbolvar,
                values=range(0,maxatoms+1),
                command=self.nsymbol_action)
        self.nsymbol.config(width=5)

        self.nsymbollabel.pack(side=tk.LEFT)
        self.nsymbol.pack(side=tk.LEFT)

        self.nsymbolfrm.grid(row=prow, column=0, columnspan=8, sticky=tk.W)
        prow += 1

        # generate widgets
        self.widgets = []

        for i in range(maxatoms):
            # symbol
            symbol = tktool.TruncatedEntry(self, limitwidth=2, width=3)
            # fill button
            fill = tk.Button(self, text='>',
                    command=self.fill_by_symbol_skel(i))
            # z
            z = tktool.validateentry.IntPositive(self, width=8)
            # w
            w = tktool.validateentry.DoublePositive(self, width=8)

            # stoichiometry
            stoich = tktool.validateentry.DoubleZeroPositive(self, width=8)

            # displacement
            disp = tktool.validateentry.Vec3d(self)
            disp.config(width=5)

            self.widgets.append({'symbol':symbol, 'fill':fill, 'z':z, 'w':w,
                'stoich':stoich, 'disp':disp})

        # layout widgets with labels
        #
        #   | sym | (fill button) | z | m | (pad) | stoich | (pad) | Damage
        # --+-----+---------------+---+---+-------+--------+-------+-------
        #  1| ....|


        # header
        tk.Label(self, text='Sym.').grid(row=prow, column=1, sticky=tk.S)
        tk.Label(self, text='z').grid(row=prow, column=3, sticky=tk.S)
        tk.Label(self, text='w').grid(row=prow, column=4, sticky=tk.S)
        tk.Label(self, text='Stoich.').grid(row=prow, column=6, sticky=tk.S)
        tk.Label(self, text='Damage(eV)\ndisp. / latt. / surf.').grid(row=prow, column=8)

        prow += 1
        for i in range(maxatoms):
            # label
            tk.Label(self, text='{0:d}'.format(i+1)).grid(row=prow, column=0)

            self.widgets[i]['symbol'].grid(row=prow, column=1)
            self.widgets[i]['fill'].grid(row=prow, column=2)
            self.widgets[i]['z'].grid(row=prow, column=3)
            self.widgets[i]['w'].grid(row=prow, column=4)
            tk.Frame(self, width='10').grid(row=prow, column=5)
            self.widgets[i]['stoich'].grid(row=prow, column=6)
            tk.Frame(self, width='10').grid(row=prow, column=7)
            self.widgets[i]['disp'].grid(row=prow, column=8)

            prow += 1

        # set valid entries
        self.clear()

    def fill_by_symbol_skel(self, index):
        def fill_by_symbol():
            symbol = self.widgets[index]['symbol'].get()
            if symbol in elem.table_bysym:
                e = elem.table_bysym[symbol]
                self.widgets[index]['z'].set(e.z)
                self.widgets[index]['w'].set(e.mass)
                # disp
                self.widgets[index]['disp'].set(disp.disp.get(symbol,
                            disp.default))
        return fill_by_symbol

    def set(self, d):
        # decide nsymbol
        self.nsymbolvar.set(min(len(d), maxatoms))

        nsymbol = self.nsymbolvar.get()

        # valid widgets
        for i in range(nsymbol):
            self.widgets[i]['symbol'].set(d[i].get('symbol',
                defaultparam_elem['symbol']))
            self.widgets[i]['z'].set(d[i].get('z',
                defaultparam_elem['z']))
            self.widgets[i]['w'].set(d[i].get('w',
                defaultparam_elem['w']))
            self.widgets[i]['stoich'].set(d[i].get('stoich',
                defaultparam_elem['stoich']))
            self.widgets[i]['disp'].set(d[i].get('disp',
                defaultparam_elem['disp']))
            self._enable_elem(i)

        # invalid widgets
        for i in range(nsymbol, maxatoms):
            self.widgets[i]['symbol'].set(defaultparam_elem['symbol'])
            self.widgets[i]['z'].set(defaultparam_elem['z'])
            self.widgets[i]['w'].set(defaultparam_elem['w'])
            self.widgets[i]['stoich'].set(defaultparam_elem['stoich'])
            self.widgets[i]['disp'].set(defaultparam_elem['disp'])
            self._disable_elem(i)

    def _enable_elem(self, i):
        """enable i-th atom element, but this is allowed when whole frame
        is enabled
        """
        if self.is_disabled():
            return
        self.widgets[i]['symbol'].config(state='normal')
        self.widgets[i]['fill'].config(state='normal')
        self.widgets[i]['z'].config(state='normal')
        self.widgets[i]['w'].config(state='normal')
        self.widgets[i]['stoich'].config(state='normal')
        self.widgets[i]['disp'].config(state='normal')

    def _disable_elem(self, i):
        """enable i-th atom element"""
        self.widgets[i]['symbol'].config(state='disabled')
        self.widgets[i]['fill'].config(state='disabled')
        self.widgets[i]['z'].config(state='disabled')
        self.widgets[i]['w'].config(state='disabled')
        self.widgets[i]['stoich'].config(state='disabled')
        self.widgets[i]['disp'].config(state='disabled')

    def _set_nsymbol(self, v):
        """change number of valid atom symbol widgets
        contents of atom symbol widgets are not changed.
        """
        # cap v range to [0..maxatoms]
        if v < 0:
            self.nsymbolvar.set(0)
        elif v > maxatoms:
            self.nsymbolvar.set(maxatoms)
        else:
            self.nsymbolvar.set(v)

        nsymbol = self.nsymbolvar.get()

        for i in range(maxatoms):
            if i < nsymbol:
                self._enable_elem(i)
            else:
                self._disable_elem(i)

    def nsymbol_action(self):
        """called when klay spinbox is changed"""
        self._set_nsymbol(self.nsymbolvar.get())

    def get(self):
        if self.is_disabled():
            return None
        d = []
        for i in range(self.nsymbolvar.get()):
            d.append({
                'symbol':self.widgets[i]['symbol'].get(),
                'z':self.widgets[i]['z'].get(),
                'w':self.widgets[i]['w'].get(),
                'stoich':self.widgets[i]['stoich'].get(),
                'disp':self.widgets[i]['disp'].get()})
        return d

    def get_nostatechk(self):
        d = []
        for i in range(self.nsymbolvar.get()):
            d.append({
                'symbol':self.widgets[i]['symbol'].get_nostatechk(),
                'z':self.widgets[i]['z'].get_nostatechk(),
                'w':self.widgets[i]['w'].get_nostatechk(),
                'stoich':self.widgets[i]['stoich'].get_nostatechk(),
                'disp':self.widgets[i]['disp'].get_nostatechk()})
        return d

    def clear(self):
        self.set([])

    def enable(self):
        self.disabled = False
        self.nsymbol.config(state=tk.NORMAL)
        nsymbol = self.nsymbolvar.get()
        for i in range(maxatoms):
            if i < nsymbol:
                self._enable_elem(i)
            else:
                self._disable_elem(i)

    def disable(self):
        self.nsymbol.config(state=tk.DISABLED)
        for i in range(maxatoms):
            self._disable_elem(i)
        self.disabled = True

    def is_disabled(self):
        return self.disabled

    @staticmethod
    def validate_wunit(w):
        """
        @param w widget mapping
        """
        err = []
        # test 'symbol' should be 1 or 2 characters
        try:
            v = w['symbol'].get()
            if len(v) < 1 or len(v) > 2:
                stat = False
                err.append(('symbol', 'char length is not valid'))
        except:
            err.append(('symbol', 'exception orruced'))

        # test z, w, stoich and disp
        for name in ['z', 'w', 'stoich', 'disp']:
            e = w[name].validate()
            if e:
                err.append((name, e))

        return err if err else None


    def validate(self):
        if self.is_disabled():
            return None

        err = []
        for i in range(self.nsymbolvar.get()):
            e = self.validate_wunit(self.widgets[i])
            if e:
                err.append(('atom {0:d}'.format(i+1), e))

        return err if err else None


if __name__ == '__main__':
    import tktool.gui_testframe as gt

    app = tk.Tk()

    gt.gui_testframe(app, AtomTbl, exampleparam)

    app.mainloop()
