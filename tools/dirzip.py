import os
import zipfile

def dirzip(dirname, verbose=False):
    """
        zip /path/to/dirname to /path/to/dirname.zip
        dirname.zip is overwritten
    """

    # test argument is dir ?
    if not os.path.isdir(dirname):
        raise Exception('{} is not directory'.format(dirname))

    bname = os.path.basename(dirname)

    # is bname is regular directory name?
    if bname in ('', '.', '..'):
        raise Exception('basename of ({}) is invalid'.format(dirname))
    
    #absdirname = os.path.abspath(dirname)
    #abszipname = absdirname + '.zip'
    zipname = dirname + '.zip'

    with zipfile.ZipFile(zipname, 'w') as z:
        for dirpath, dirnames, filenames in os.walk(dirname):
            for f in filenames:
                archpath = os.path.join(dirpath, f)
                archname = os.path.relpath(archpath, dirname)
                if verbose:
                    print zipname, ':', archname
                z.write(archpath, archname)

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('dirs', metavar='DIR', type=str, nargs='+',
            help='directory to make directory.zip')
    parser.add_argument('--verbose', '-v', action='store_true',
            default=False, help='verbose mode')

    args = parser.parse_args()

    for d in args.dirs:
        print 'zipping', d
        try:
            dirzip(d, args.verbose)
        except Exception as e:
            print ' error, skipped', str(e)

