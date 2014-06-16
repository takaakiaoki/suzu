@rem cmdline option
@set setupopt=-q
@if "%1" == "-v" set setupopt=-v
@if "%1" == "/v" set setupopt=-v
@echo %setupopt%

rem get suzu version
@for /f usebackq %%i in (`python tools\suzu_version.py`) do (@set SUZUVER=%%i)
@echo VERSION=%SUZUVER%

@rem create .html from README files
rst2html.py README README.html
rst2html.py README-ja.rst README-ja.html
cd suzu\doc
@call make.bat
cd ..\..

@rem create python package
python setup.py %setupopt% sdist --formats=zip
python setup_cx.py %setupopt% bdist_msi

@rem web pabe contents
mkdir html
mkdir html\dist
@rem README-ja.html -> index-ja.html
python tools\readme2index.py --ienc=utf-8 --oenc=utf-8 README.html html\index.html
@rem README-ja.html -> index-ja.html
python tools\readme2index.py --ienc=utf-8 --oenc=utf-8 README-ja.html html\index-ja.html
for %%i in (-win32.msi, -amd64.msi, .zip) do copy dist\suzu-%SUZUVER%%%i html\dist

:end
