import sys
import os
from cx_Freeze import setup, Executable

ver_file = os.path.join(os.path.dirname(__file__), 'dummy_tin', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

# we need to include tix libs explicitly
build_exe_options = {
        #'include_files':[('dummy_tin/doc/*.rst', 'doc'),
        #    ('dummy_tin/doc/*.html', 'doc')]
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
    executables = [Executable('suzu.py', base='Win32GUI')])
