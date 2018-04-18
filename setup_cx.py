import sys
import os
import glob

from cx_Freeze import setup, Executable

from tools.find_in_pathenv import find_in_pathenv

ver_file = os.path.join(os.path.dirname(__file__), 'suzu', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

def create_include_tix():
    """ find tixxx.dll and related files, manually
    see http://www.py2exe.org/index.cgi/TixSetup 
    """
    # get tcl/tk install information
    import tkinter
    import _tkinter

    tk = _tkinter.create()
    # get tcl, tk, tix versions
    tcl_version = _tkinter.TCL_VERSION 
    tk_version = _tkinter.TK_VERSION 
    tix_version = tk.call('package', 'version', 'Tix')

    # get tcl and tk library directory
    # see https://stackoverflow.com/questions/35533803/keyerror-tcl-library-when-i-use-cx-freeze
    tcl_dir = tk.exprstring('$tcl_library')
    tk_dir = tk.exprstring('$tk_library')

    del tkinter, _tkinter

    print('tcl_version = ', tcl_version)
    print('tk_version = ', tk_version)
    print('tix_version = ', tix_version)
    print('tcl_dir = ', tcl_dir)
    print('tk_dir = ', tk_dir)

    includelist = []

    # set os.environ, 
    # see https://stackoverflow.com/questions/35533803/keyerror-tcl-library-when-i-use-cx-freeze
    os.environ['TCL_LIBRARY'] = tcl_dir
    os.environ['TK_LIBRARY'] = tk_dir

    # tcl and tk dlls
    tcldllpath = find_in_pathenv('tcl{}t.dll'.format(tcl_version.replace('.', '')))

    if tcldllpath is None:
        raise 'tcl{xx}t.dll is not found'

    tkdllpath = find_in_pathenv('tk{}t.dll'.format(tk_version.replace('.', '')))
    if tkdllpath is None:
        raise 'tk{xx}t.dll is not found'

    # try to find tix directory
    tix_basename = 'tix{}'.format(tix_version)
    tix_dir = os.path.join(os.path.dirname(tcl_dir), tix_basename)
    print('tix_dir = ', tix_dir)
    if not os.path.isdir(tix_dir):
        raise 'tix_dir does not exist.'

    return [str(tcldllpath), str(tkdllpath), (tix_dir, tix_basename)]

def create_include_doc():
    htmls = glob.glob('suzu/doc/*.html')
    rsts = glob.glob('suzu/doc/*.rst')
    fs = []
    for f in htmls + rsts:
        basename = os.path.basename(f)
        fs.append((f, os.path.join('doc', basename)))
    return fs

include_files = [('README.rst','README.rst'), ('README.html','README.html'),
        ('README-ja.rst','README-ja.rst'), ('README-ja.html','README-ja.html')] \
        + create_include_doc() + create_include_tix()
# modules?
includes = []
excludes = []
# 3rd party packages it would be better than using requires given by distutils?
packages = ['lockfile']

# we need to include tix libs explicitly
build_exe_options = {
        'include_files':include_files,
        'includes':includes,
        'excludes':excludes,
        'packages':packages
        }

setup(name = "suzu",
    version = vars['__version__'],
    description = "Yet another UI program for SRIM parameter input program (tin.exe)",
    author = "Takaaki AOKI",
    author_email = "aoki.takaaki.6v@kyoto-u.ac.jp",
    url = "https://github.com/takaakiaoki/suzu",
    # download_url = "https://github.com/takaakiaoki/suzu",
    long_description=open('README.rst').read(),
    # cx_Freeze option
    options={'build_exe':build_exe_options},
    executables = [Executable('suzu.py', base='Console')]
    )
