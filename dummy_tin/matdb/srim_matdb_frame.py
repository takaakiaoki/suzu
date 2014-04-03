import tkinter.messagebox
import tkinter.tix as tix

from . import matdb_frame
from . import srim_compounddb

from ..tktool import filepathentry

def _entries_from_srim(srim_data_path):
    """
    @param srim_data_path path to SRIM compound db (SRIM_PATH/Data/Compound.dat),
                          usually encoded in cp437
    """
    try:
        categories = srim_compounddb.parse(open(srim_data_path, 'rt', encoding='cp437'))
        entries = []
        for cindex, c in enumerate(categories):
            cpath = str(cindex)
            ctitle = c.get_title()
            csummary = c.desc
            # no content
            entries.append({'path':cpath, 'title':ctitle, 'summary':csummary})
            # table element
            for tindex, t in enumerate(c.tables):
                path = '.'.join((cpath, str(tindex)))
                title = t.name
                summary = srim_compounddb.format_compound(t)
                content = t.to_suzu()
                entries.append({'path':path, 'title':title,
                    'summary':summary, 'content':content})
            # replace contents

        return entries
    except Exception as e:
        raise e


class SRIMMatDBFrame(tix.Frame):
    class Open(filepathentry.Open):
        def on_fileselected(self, newpath, oldpath):
            if self.master.load_srimdata:
                self.master.load_srimdata(newpath)

    def __init__(self, master, srimdata=None, title=None):
        """
        @param master master widget
        @param srimdata path to SRIM compound db, usually encoded in cp437
        @param title title of the widget
        """
        tix.Frame.__init__(self, master, title)

        # filepath entry
        label = tix.Label(self, text='SRIM compound.dat:')
        label.grid(row=0, column=0, sticky='W')
        self.filepath = SRIMMatDBFrame.Open(self, label='open SRIM compound.dat')
        self.filepath.filepath.config(stat=tix.DISABLED)

        self.filepath.grid(row=1, column=0, sticky='WE', padx=(10, 0))
        # data selection table
        self.dselect = matdb_frame.MatDBFrame(self)
        self.dselect.grid(row=2, column=0, sticky='WENS')

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        if srimdata:
            self.load_srimdata(srimdata)

    def load_srimdata(self, path):
        """
        @param self
        @param srimdata path to SRIM compound db, usually encoded in cp437
        """
        try:
            self.dselect.set_listbox_entries(_entries_from_srim(path))
            self.filepath.set(path)
        except Exception as e:
            tkinter.messagebox.showerror('error on loading SRIM compound data',
                    'error on loading SRIM compound data.\n{}\n'.format(path)+ repr(e))
