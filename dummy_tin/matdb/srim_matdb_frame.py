import Tix as tix

import matdb_frame
import srim_compounddb

from ..tktool import filepathentry

def _entries_from_srim(srim_data_path):
    try:
        categories = srim_compounddb.parse(open(srim_data_path, 'rt'))
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
            try:
                if self.master.load_srimdata:
                    self.master.load_srimdata(newpath)
                    self.set(newpath) # verborse operation ...
            except Exception as e:
                self.set(oldpath)
                raise e

    def __init__(self, parent, srimdata=None, title=None):
        tix.Frame.__init__(self, parent, title)

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
        self.dselect.set_listbox_entries(_entries_from_srim(path))
        self.filepath.set(path)
