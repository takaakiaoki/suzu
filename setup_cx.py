import sys
import os
import glob

from cx_Freeze import setup, Executable

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

    # get tcl library directory
    tcl_dir = tk.call('info', 'library')

    del tkinter, _tkinter

    print('tcl_version = ', tcl_version)
    print('tk_version = ', tk_version)
    print('tix_version = ', tix_version)
    print('tcl_dir = ', tcl_dir)

    # try to find tix directory
    tix_basename = 'tix{}'.format(tix_version)
    tix_dir = os.path.join(os.path.dirname(tcl_dir), tix_basename)
    print('tix_dir = ', tix_dir)
    if os.path.isdir(tix_dir):
        return [(tix_dir, tix_basename)]
    else:
        print('tix_dir does not exist.')

    return []

def create_include_doc():
    htmls = glob.glob('suzu/doc/*.html')
    rsts = glob.glob('suzu/doc/*.rst')
    fs = []
    for f in htmls + rsts:
        basename = os.path.basename(f)
        fs.append((f, os.path.join('doc', basename)))
    return fs

include_files = [('README','README'), ('README.html','README.html'),
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
    description = "fake UI program for SRIM parameter input program (tin.exe)",
    author = "Takaaki AOKI",
    author_email = "aoki@sakura.nucleng.kyoto-u.ac.jp",
    url = "http://sakura.nucleng.kyoto-u.ac.jp/~aoki/suzu/",
    download_url = "http://sakura.nucleng.kyoto-u.ac.jp/~aoki/hg/suzu/",
    long_description=open('README').read(),
    # cx_Freeze option
    options={'build_exe':build_exe_options},
    executables = [Executable('suzu.py', base='Console')]
    )
