import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../../..'))

import Tix as tix

import dummy_tin.matdb.matdb as matdb
import dummy_tin.matdb.srim_compounddb as compounddb

if __name__ == '__main__':
    app = tix.Tk()

    # entries
    # {'path':, 'path of Hlist seperated with '.'}
    #   'title': string shown at listbox
    #   'summary': texts shown in summary field
    #   'content': (optional) value to be returend
    #              (None is allowed, and applied for directory entry for example)
    #}
    entries = [
        {'path':"A", 'title':'A', 'summary':'Directory A'},
        {'path':"A.B", 'title':'B', 'summary':'summary of B', 'content':11},
        {'path':"A.C", 'title':'C', 'summary':'summary of C', 'content':12},
        {'path':"A.D", 'title':'D', 'summary':'summary of D', 'content':13},
        {'path':"A.E", 'title':'E', 'summary':'summary of E', 'content':14},
        {'path':"F", 'title':'F', 'summary':'Directory F'},
        {'path':"F.G", 'title':'G', 'summary':'summary of G', 'content':21},
        {'path':"F.H", 'title':'H', 'summary':'summary of H', 'content':22},
        {'path':"F.I", 'title':'I', 'summary':'Directory F.I'},
        {'path':"F.I.J", 'title':'J', 'summary':'summary of J', 'content':231},
        {'path':"F.I.K", 'title':'K', 'summary':'summary of K', 'content':232},
        {'path':"L", 'title':'L', 'summary':'Directory L'},
        {'path':"L.M", 'title':'M', 'summary':'summary of M', 'content':31},
        {'path':"L.N", 'title':'N', 'summary':
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
a''', 'content':32}]

    # test for less entries
    #del(entries[3:])

    def entries_from_srim(srim_data_path):
        categories = compounddb.parse(open(srim_data_path, 'rt'))
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
                summary = compounddb.format_compound(t)
                content = t.to_suzu()
                entries.append({'path':path, 'title':title,
                    'summary':summary, 'content':content})
            # replace contents

        return entries

    entries = entries_from_srim(os.path.join(os.path.dirname(__file__),'../Compound.dat'))

    d = matdb.Dialog(app, entries)

    app.wait_window(d)
    print d.result

    #app.mainloop()
