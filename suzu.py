#!/usr/bin/env python

import Tkinter as tk
import dummy_tin.gui_root

app = tk.Tk()

root = dummy_tin.gui_root.Root(app)
root.pack()

app.mainloop()
