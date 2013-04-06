rem get suzu version
for /f usebackq %%1 in (`python tools\suzu_version.py`) do (@set SUZUVER=%%1)

echo %SUZUVER%

rem create .html from README.rst files
rst2html.py README README.html
cd dummy_tin\doc
call make.bat
cd ..\..

rem create python package
python setup.py sdist --formats=zip,gztar
python setup.py bdist_wininst
python setup.py py2exe

rem compress w32standalone
python tools\dirzip.py dist\suzu-%SUZUVER%.w32standalone
