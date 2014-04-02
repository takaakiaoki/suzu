import sys
import os
from distutils.core import setup
import glob

ver_file = os.path.join(os.path.dirname(__file__), 'dummy_tin', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

docfiles = glob.glob('doc/*.rst')
    
setup(name = "suzu",
    version = vars['__version__'],
    description = "fake UI program for SRIM parameter input program (tin.exe)",
    author = "Takaaki AOKI",
    author_email = "aoki@sakura.nucleng.kyoto-u.ac.jp",
    url = "http://sakura.nucleng.kyoto-u.ac.jp/~aoki/suzu/",
    download_url = "http://sakura.nucleng.kyoto-u.ac.jp/~aoki/hg/suzu/",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['dummy_tin', 'dummy_tin.tktool', 'dummy_tin.physics',
        'dummy_tin.db', 'dummy_tin.context'],
    package_dir = {'dummy_tin':'dummy_tin'},
    package_data = {'dummy_tin':['doc/*.rst', 'doc/*.html']},
    scripts = ["suzu.py"],
    long_description=open('README').read(),
    options={},
    #This next part it for the Cheese Shop, look a little down the page.
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Scientiric/Engineering :: Physics",
        ]
) 
