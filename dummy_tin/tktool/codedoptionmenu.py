""" extention of tk.OptionMenu which takes of pairs of (value, text)
"""

import Tkinter as tk


class CodedOptionMenu(tk.OptionMenu):
    """ extention of tk.OptionMenu which takes of pairs of (value, text)
    """
    def __init__(self, master, options, **kw):
        self.cv = tk.StringVar(master)

        self.setup_optionparam(options)

        tk.OptionMenu.__init__(self, master, self.cv, *self.texts, **kw)

    def set(self, v):
        self.cv.set(self.v_to_text[v])

    def get(self):
        return self.text_to_v[self.cv.get()]

    def get_nostatechk(self):
        return self.text_to_v[self.cv.get()]

    def clear(self):
        pass

    def setup_optionparam(self, options):
        """initialize self.v_to_text, self.text_to_v, and self.texts
        """
        self.v_to_text = {}
        self.text_to_v = {}
        self.texts = []
        for v, t in options:
            self.v_to_text[v] = t
            self.text_to_v[t] = v
            self.texts.append(t)

    def set_new_option(self, options, command=None):
        """delete current options and set new options. variable does not change"""
        # delete current all menuoptions
        if len(self.texts):
            self['menu'].delete(0, len(self.texts))
        # create new textoption and translation tables
        self.setup_optionparam(options)

        # register self.text as menu, see source of Tkinter.OptionMenu.__init__
        for v in self.texts:
            self['menu'].add_command(label=v,
                    command=tk._setit(self.cv, v, command))

    def validate(self):
        return None

    def enable(self):
        self.config(state=tk.NORMAL)

    def disable(self):
        self.config(state=tk.DISABLED)

    def is_disabled(self):
        return self.cget('state') == tk.DISABLED

        
if __name__ == '__main__':
    app = tk.Tk()

    option1 = [(1, 'one'), (2, 'two'), (3, 'three'), (0, 'zero')]
    option2 = [(9, 'nine'), (8, 'eight'), (7, 'seven'), (6, 'six')]
    option = option1
    menu = CodedOptionMenu(app, option)

    # can I change the property menu?
    menu.config(width=30, anchor='e')
    menu.pack()

    def set_action():
        menu.set(0)
    set_btn = tk.Button(app, text='set', command=set_action)
    set_btn.pack()

    def get_action():
        print menu.get()
    get_btn = tk.Button(app, text='get', command=get_action)
    get_btn.pack()

    def switch_action():
        global option
        if option == option1:
            option = option2
        else:
            option = option1
        menu.set_new_option(option)

    switch_btn = tk.Button(app, text='switch', command=switch_action)
    switch_btn.pack()

    app.mainloop()
