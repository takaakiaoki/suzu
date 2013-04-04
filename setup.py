import sys
import os
from distutils.core import setup

# Test ttk installation. This check is needed only for python 2.6,
# for python 2.7 ttk is a pre-installed package
# for python 3.x tkinter.ttk will be available
try:
    import ttk
except:
    print """Failed to "import ttk". Please install "pyttk" package by
    - easy_install pyttk (or pip install pyttk)
    - (or download from http://pypi.python.org/pypi/pyttk directly)
    """
    sys.exit(2)

try:
    import py2exe
except:
    print >> sys.stderr, 'warning, import py2exe failed, this feature is not available now'

ver_file = os.path.join('dummy_tin', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)
    
setup(name = "suzu",
    version = vars['__version__'],
    description = "fake UI program for SRIM parameter input program (tin.exe)",
    author = "Takaaki AOKI",
    author_email = "aoki@sakura.nucleng.kyoto-u.ac.jp",
    url = "not yet",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['dummy_tin', 'dummy_tin.tktool'],
    package_dir = {'dummy_tin':'dummy_tin'},
    package_data = {'dummy_tin':['doc/*']},
    #'runner' is in the root.
    scripts = ["suzu.py"],
    long_description = """ """,
    # py2exe option
    console=["suzu.py"],
    options={'py2exe':{
            'optimize':2,
            'dist_dir':'dist/suzu-{0:s}.w32standalone'.format(vars['__version__'])}}
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []
) 
