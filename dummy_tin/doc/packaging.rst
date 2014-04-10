=========
Packaging
=========

Create .zip package
====================

.. code-block:: console

  python setup.py sdist

Archived packages are created as dist/suzu-(version).zip .
These packages can be installed using easy_install (a part of setuptools http://pypi.python.org/pypi/setuptools) or pip (http://pypi.python.org/pypi/pip)

with easy_install

.. code-block:: console

  easy_install <path to .zip>

with pip

.. code-block:: console

  pip install <path to .zip>

Create w32 standalone package
=============================

cs_Freeze (http://cx-freeze.sourceforge.net/) and pywin32 (http://sourceforge.net/projects/pywin32/) should be set up to build w32 standalone package

.. code-block:: console

  python setup_cx.py bdist_msi

Standalone package is created as dist/suzu-(version)-win32.msi or -amd64.msi . 

