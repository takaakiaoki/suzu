=========
Packaging
=========

Create .exe installer
=====================

::

  python setup.py bdist_wininst

.exe installer is created as dist/suzu-(version).win32.exe

Create .zip, or tar.gz package
==============================

::
  python setup.py sdist --format=zip,targz

Archived packages are created as dist/suzu-(version).tar.gz or dist/suzu-(version).zip
These packages can be installed using easy_install (a part of setuptools http://pypi.python.org/pypi/setuptools) or pip (http://pypi.python.org/pypi/pip/1.2.1)

with easy_install ::

  easy_install <path to .zip or .tar.gz>

with pip ::

  pip install <path to .zip or .tar.gz>

Create w32 standalone package
=============================

Use py2exe (http://www.py2exe.org) package.

::
  python setup.py py2exe

Stand alone package is created as dist/suzu-(version).w32standalone .
