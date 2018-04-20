====
SUZU
====

version 0.4.1

April 18, 2018

Takaaki AOKI (aoki.takaaki.6v@kyoto-u.ac.jp)

`Japanese <README-ja.html>`_

.. contents::
  :local:

About SUZU
==========

SRIM (http://www.srim.org/) is the most famous software to simulate the trajectroy and radiation effects of energetic particles in various materials. SRIM is equped with well-made GUI program for parameter setup (TIN.exe), however, it cannot run correctly on the Windows OS based multibyte characters, such as Japanese. SUZU (a japanese tranlation of tin :-) is aimed to be a gui program with compatible functions to tin.exe and run on multilingual windows (and possibly other OS platforms). 

Install & Run
=============

For windows, two options are available to setup this program.
The second option is also available for unix or mac user.

Option 1: Use standalone package (for Windows)
-----------------------------------------------

1. Download Standalone package

   Go to https://github.com/takaakiaoki/suzu/releases , download suzu-(version)-win32.exe, or suzu-(version)-win-amd64.exe, and run it. Softwares are expanded at appropriate place, such as C:\\Program Files\\suzu, and the shortcut is added on the start menu.

2. Run

  Find and Double-click suzu.exe  

Option 2: Install as python script and package
----------------------------------------------

The second option is installing suzu as a package of python library.
suzu version >= 0.1.0 is developed to run on python 3.3.5 (or above). Setup python core program from http://www.python.org/

suzu is available at PyPI (https://pypi.org/project/suzu/), then

.. code-block::

    pip install suzu

Run
+++

- type suzu in command prompt
- or, find suzu executable file (i.e. C:\\Python33\\Script\\suzu.exe) and double-click it.

Source code repository
======================

Source code is maintaned at https://github.com/takaakiaoki/suzu

Code is managed using git (https://git-scm.com/). So you can access the latest source code set by ...

.. code-block:: console

   git clone https://github.com/takaakiaoki/suzu.git

or

.. code-block:: console

   git clone git@github.com/takaakiaoki/suzu.git

, or you may freely fork and modify it.


Usage
=====

[Save (&Run Trim)]
-------------------

Fill parameters as you like and push [Save (& Run Trim)] button.

When you save the data with the filename of 'TRIM.in' and you put it in the same folder where TRIM.exe exists 
(== where SRIM is setup), a dialog window pops-up to confirm run TRIM.exe calculation with this new TRIM data.

[Load .json]
------------

Currently suzu cannot parse TRIM.in format directly, but suzu saves TRIM.in.json data with TRIM.in simultaneously.
You may load this .json file by [Load .json] button.

[Validate]
----------

[Validate] button tests a contents of widgets. This validation routine also runs before [Save (&Run Trim)] action.

.. note::

  Validation does not run automatically. The user should push
  [Validate] button explicitly to confirm the modification on GUI 
  is correct or not.

[Compound DB]
-------------

[Compount DB] button is placed at target layer frame. This button provides an access to the compoond database given by SRIM.
At database dialog, indicate the path to compound.dat (usually, [SRIM INSTALL PATH]/DATA/Compound.dat). You may construct your own database.


Other Buttons
-------------

[Set Example] [Dump to Console] [Clear] buttons still remains for debugging.

More Information
================

Detail information especially for developers are found in dummy_tin/doc/* (python script package).


Bugs, issues, discussion for developers
=======================================

The author is pleased to here bug & issue reports and suggest & request for the software.
