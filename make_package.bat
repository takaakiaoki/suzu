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
python setup.py %setupopt% sdist --formats=zip
@rem python setup.py %setupopt% bdist_wininst
python setup_cx.py %setupopt% build_exe
python setup_cx.py %setupopt% bdist_msi

@rem compress w32standalone
@rem python tools\dirzip.py dist\suzu-%SUZUVER%.w32standalone

@rem web pabe contents
mkdir html
mkdir html\dist
copy README.html html\index.html
@rem for %%i in (msi, w32standalone.zip, win32.exe, tar.gz, zip) do copy dist\suzu-%SUZUVER%.%%i html\dist

:end
