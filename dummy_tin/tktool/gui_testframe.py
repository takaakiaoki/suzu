import tkinter as tk

from . import codedoptionmenu as co

def gui_testframe(master, FrameClass, example=None):
    """setup test window,
        1. put gui frame
        2. put action buttons, 
           - set_example (FrameClass.set())
           - get (FrameClass.get())
           - clear (FrameClass.clear())
           - validate (FrameClass.validate())
           - enable (FrameClass.enable())
           - disable (FrameClass.disable())
    """

    gui = FrameClass(master)
    gui.pack(side=tk.TOP)

    buttonframe = tk.Frame(master)

    # set example 
    def set_action():
        gui.set(example)
    setbtn = tk.Button(buttonframe, text='set example', command=set_action)
    setbtn.pack(side=tk.LEFT, pady=2)
    # get
    def get_action():
        print(gui.get())
    getbtn = tk.Button(buttonframe, text='get', command=get_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # get_nostatechk
    def get_nostatechk_action():
        print(gui.get_nostatechk())
    getbtn = tk.Button(buttonframe, text='get_nostatechk', command=get_nostatechk_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # clear
    def clear_action():
        gui.clear()
    clearbtn = tk.Button(buttonframe, text='clear', command=clear_action)
    clearbtn.pack(side=tk.LEFT, pady=2)
    # validate
    def validate_action():
        print(gui.validate())
    getbtn = tk.Button(buttonframe, text='validate', command=validate_action)
    getbtn.pack(side=tk.LEFT, pady=2)

    # enable
    def enable_action():
        gui.enable()
    enablebtn = tk.Button(buttonframe, text='enable', command=enable_action)
    enablebtn.pack(side=tk.LEFT, pady=2)

    # disable
    def disable_action():
        gui.disable()
    disablebtn = tk.Button(buttonframe, text='disable', command=disable_action)
    disablebtn.pack(side=tk.LEFT, pady=2)

    buttonframe.pack(side=tk.TOP)


def gui_testframe_multiexam(master, FrameClass, examples=[]):
    """setup test window,
        1. put gui frame
        2. put action buttons, 
           - set_example (FrameClass.set())
           - get (FrameClass.get())
           - clear (FrameClass.clear())
           - validate (FrameClass.validate())
           - enable (FrameClass.enable())
           - disable (FrameClass.disable())
        examples is a list of tuple, [(title, exampledata), ...]
    """

    # title -> index mappin
    example_option = [(i, t) for (i, (t, d)) in enumerate(examples)]

    gui = FrameClass(master)
    gui.pack(side=tk.TOP)

    buttonframe = tk.Frame(master)

    selectlabel = tk.Label(buttonframe, text='Example:')
    selectlabel.pack(side=tk.LEFT)

    # set default
    def select_action(textvalue):
        gui.set(examples[select.get()][1])

    select = co.CodedOptionMenu(buttonframe, example_option, command=select_action)
    select.config(width=20, anchor=tk.W, justify=tk.LEFT)
    select.pack(side=tk.LEFT, pady=2)

    # get
    def get_action():
        print(gui.get())
    getbtn = tk.Button(buttonframe, text='get', command=get_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # get_nostatechk
    def get_nostatechk_action():
        print(gui.get_nostatechk())
    getbtn = tk.Button(buttonframe, text='get_nostatechk', command=get_nostatechk_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # clear
    def clear_action():
        gui.clear()
    clearbtn = tk.Button(buttonframe, text='clear', command=clear_action)
    clearbtn.pack(side=tk.LEFT, pady=2)
    # validate
    def validate_action():
        print(gui.validate())
    getbtn = tk.Button(buttonframe, text='validate', command=validate_action)
    getbtn.pack(side=tk.LEFT, pady=2)

    # enable
    def enable_action():
        gui.enable()
    enablebtn = tk.Button(buttonframe, text='enable', command=enable_action)
    enablebtn.pack(side=tk.LEFT, pady=2)

    # disable
    def disable_action():
        gui.disable()
    disablebtn = tk.Button(buttonframe, text='disable', command=disable_action)
    disablebtn.pack(side=tk.LEFT, pady=2)

    buttonframe.pack(side=tk.TOP)

def gui_testframe(master, FrameClass, example=None):
    """setup test window,
        1. put gui frame
        2. put action buttons, 
           - set_example (FrameClass.set())
           - get (FrameClass.get())
           - clear (FrameClass.clear())
           - validate (FrameClass.validate())
           - enable (FrameClass.enable())
           - disable (FrameClass.disable())
        example is a list of tuple [(title, exampledata)]
    """

    gui = FrameClass(master)
    gui.pack(side=tk.TOP)

    buttonframe = tk.Frame(master)

    # set example 
    def set_action():
        gui.set(example)
    setbtn = tk.Button(buttonframe, text='set example', command=set_action)
    setbtn.pack(side=tk.LEFT, pady=2)
    # get
    def get_action():
        print(gui.get())
    getbtn = tk.Button(buttonframe, text='get', command=get_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # get_nostatechk
    def get_nostatechk_action():
        print(gui.get_nostatechk())
    getbtn = tk.Button(buttonframe, text='get_nostatechk', command=get_nostatechk_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # clear
    def clear_action():
        gui.clear()
    clearbtn = tk.Button(buttonframe, text='clear', command=clear_action)
    clearbtn.pack(side=tk.LEFT, pady=2)
    # validate
    def validate_action():
        print(gui.validate())
    getbtn = tk.Button(buttonframe, text='validate', command=validate_action)
    getbtn.pack(side=tk.LEFT, pady=2)

    # enable
    def enable_action():
        gui.enable()
    enablebtn = tk.Button(buttonframe, text='enable', command=enable_action)
    enablebtn.pack(side=tk.LEFT, pady=2)

    # disable
    def disable_action():
        gui.disable()
    disablebtn = tk.Button(buttonframe, text='disable', command=disable_action)
    disablebtn.pack(side=tk.LEFT, pady=2)

    buttonframe.pack(side=tk.TOP)
