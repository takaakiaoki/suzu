import os
import pathlib

def find_in_pathenv(filename):
    '''find first filename in PATH environment variable

    Args:
        filename (str): filename to find

    Return:
        (pathlib.Path): path to be found first
        None: filename is not found
        '''
    for p in os.environ['PATH'].split(os.pathsep):
        f = pathlib.Path(p) / filename
        if f.exists():
            return f

    return None

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=str,
            help='filenames to find')

    args = parser.parse_args()

    for f in args.files:
        p = find_in_pathenv(f)
        print(f, ':', str(p))
