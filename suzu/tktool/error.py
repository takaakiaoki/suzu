""" gui error
"""

import tkinter.messagebox

def walk_errorstruct(err, root=''):
    """ unfold error reason structure
    @param err error struct which is 
        errorstruct ::= None | msg_str | (cls_str, errorstruct) | [errorstruct]
    @param root root class name
    @return yields tuple of (class hierarchy string(dot seperated), mesg)
    """
    if err is None:
        return
    elif isinstance(err, str):
        yield root, err
    elif isinstance(err, tuple):
        for i in walk_errorstruct(err[1], root+'.'+err[0]):
            yield i
    else:
        # otherwise, err is recognized as list-like sequence
        for elems in err:
            for i in walk_errorstruct(elems, root):
                yield i

def format_errorstruct(err, max_item=7, root=''):
    # format reason
    reason = [r+': '+e for r, e in walk_errorstruct(err, root)]
    if len(reason) > max_item:
        reason = reason[:max_item]
        reason.append('.. and so on')
    return '\n'.join(reason)

def show_as_messagebox(err, max_item=7, root='', title='Validation Error'):
    tkinter.messagebox.showerror(title,
            format_errorstruct(err, max_item=max_item, root=root))
