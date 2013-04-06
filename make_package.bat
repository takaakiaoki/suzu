@rem cmdline option
@set setupopt=-q
@if "%1" == "-v" set setupopt=-v
@if "%1" == "/v" set setupopt=-v
@echo %setupopt%

rem get suzu version
@for /f usebackq %%i in (`python tools\suzu_version.py`) do (@set SUZUVER=%%i)
@echo VERSION=%SUZUVER%

@rem create .html from README.rst files
rst2html.py README README.html
cd dummy_tin\doc
@call make.bat
cd ..\..

@rem create python package
python setup.py %setupopt% sdist --formats=zip,gztar
python setup.py %setupopt% -q bdist_wininst
python setup.py %setupopt% -q py2exe

@rem compress w32standalone
python tools\dirzip.py dist\suzu-%SUZUVER%.w32standalone

:end
