===================================
Problems with virtualenv on Windows
===================================

Activate and Deactivate script
===================================

In order to use Tcl/Tk (ant Tix) library under virtualenv, some environment variables should be set explicitly.

activate.bat: ::

  @echo off
  set "VIRTUAL_ENV=C:\Users\aoki\work\marlowe_ui"

  if defined _OLD_VIRTUAL_PROMPT (
      set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
  ) else (
      if not defined PROMPT (
          set "PROMPT=$P$G"
      )
    set "_OLD_VIRTUAL_PROMPT=%PROMPT%"	
  )
  set "PROMPT=(marlowe_ui) %PROMPT%"

  if not defined _OLD_VIRTUAL_PYTHONHOME (
      set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
  )
  set PYTHONHOME=

  rem PYTHONPATH
  if not defined _OLD_VIRTUAL_PYTHONPATH (
    set "_OLD_VIRTUAL_PYTHONPATH=%PYTHONPATH%"
  )
  set PYTHONPATH=

  rem tcl/tk environment
  if not defined _OLD_VIRTUAL_TCL_LIBRARY (
    set "_OLD_VIRTUAL_TCL_LIBRARY=%TCL_LIBRARY%"
  )
  set "TCL_LIBRARY=c:\opt\python27\tcl\tcl8.5"

  if not defined _OLD_VIRTUAL_TK_LIBRARY (
    set "_OLD_VIRTUAL_TK_LIBRARY=%TCL_LIBRARY%"
  )
  set "TK_LIBRARY=c:\opt\python27\tcl\tcl8.5"

  if defined _OLD_VIRTUAL_PATH (
      set "PATH=%_OLD_VIRTUAL_PATH%"
  ) else (
      set "_OLD_VIRTUAL_PATH=%PATH%"
  )
  set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

  :END

deactivate.bat: ::

  @echo off

  if defined _OLD_VIRTUAL_PROMPT (
      set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
    set _OLD_VIRTUAL_PROMPT=
  )

  if defined _OLD_VIRTUAL_PYTHONHOME (
      set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
      set _OLD_VIRTUAL_PYTHONHOME=
  )

  rem PYTHONPATH
  if defined _OLD_VIRTUAL_PYTHONPATH (
    set "PYTHONPATH=%_OLD_VIRTUAL_PYTHONPATH%"
    set _OLD_VIRTUAL_PYTHONPATH=
  )

  rem tcl/tk environment
  set TCL_LIBRARY=
  if defined _OLD_VIRTUAL_TCL_LIBRARY (
    set "TCL_LIBRARY=%_OLD_VIRTUAL_TCL_LIBRARY%"
    set _OLD_VIRTUAL_TCL_LIBRARY=
  )
  set TK_LIBRARY=
  if defined _OLD_VIRTUAL_TK_LIBRARY (
    set "TK_LIBRARY=%_OLD_VIRTUAL_TK_LIBRARY%"
    set _OLD_VIRTUAL_TK_LIBRARY=
  )

  if defined _OLD_VIRTUAL_PATH (
      set "PATH=%_OLD_VIRTUAL_PATH%"
    set _OLD_VIRTUAL_PATH=
  )

  :END


program associated with .py
===========================

In usual case, the extension '.py' is not associated with the python.exe under virtual environment but with original one.

to confirm it ... ::

  > assoc .py
  .py=Python.File
  > ftype | findstr -i Python
  Python.CompiledFile="C:\opt\Python27\python.exe" "%1" %*
  Python.File="C:\opt\Python27\python.exe" "%1" %*
  Python.NoConFile="C:\opt\Python27\pythonw.exe" "%1" %*

Therefore, susu.py should be run in the form of 'python (path to susu.py)\susu.py' or 'python -m marlowe_ui.gui_root'
