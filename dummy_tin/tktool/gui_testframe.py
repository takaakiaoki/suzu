import Tkinter as tk

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

    # set default
    def set_action():
        gui.set(example)
    setbtn = tk.Button(buttonframe, text='set example', command=set_action)
    setbtn.pack(side=tk.LEFT, pady=2)
    # get
    def get_action():
        print gui.get()
    getbtn = tk.Button(buttonframe, text='get', command=get_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # get_nostatechk
    def get_nostatechk_action():
        print gui.get_nostatechk()
    getbtn = tk.Button(buttonframe, text='get_nostatechk', command=get_nostatechk_action)
    getbtn.pack(side=tk.LEFT, pady=2)
    # clear
    def clear_action():
        gui.clear()
    clearbtn = tk.Button(buttonframe, text='clear', command=clear_action)
    clearbtn.pack(side=tk.LEFT, pady=2)
    # validate
    def validate_action():
        print gui.validate()
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
