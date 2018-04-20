import sys
import os
from setuptools import setup, find_packages
import glob

ver_file = os.path.join(os.path.dirname(__file__), 'suzu', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

docfiles = glob.glob('doc/*.rst')
    
setup(name = "suzu",
    version = vars['__version__'],
    description = "Yet another UI program for SRIM parameter input program (tin.exe)",
    author = "Takaaki AOKI",
    author_email = "aoki.takaaki.6v@kyoto-u.ac.jp",
    url="https://github.com/takaakiaoki/suzu",
    # download_url = "https://github.com/takaakiaoki/suzu",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    #packages = ['suzu', 'suzu.tktool', 'suzu.physics',
    #    'suzu.db', 'suzu.context', 'suzu.config',
    #    'suzu.matdb'],
    packages = find_packages(),
    package_dir = {'suzu':'suzu'},
    package_data = {'suzu':['doc/*.rst', 'doc/*.html']},
    entry_points={
        'gui_scripts':[
            'suzu = suzu.run:run']},
    # scripts = ["suzu.py"],
    long_description=open('README.rst').read(),
    options={},
    install_requires=['lockfile >= 0.9.0'],
    #This next part it for the Cheese Shop, look a little down the page.
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        ]
) 
