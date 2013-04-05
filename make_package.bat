rem create .html from README.rst files
rst2html.py README.rst README.html
cd dummy_tin\doc
call make.bat
cd ..\..

rem create python package
python setup.py sdist --formats=zip,gztar
python setup.py bdist_wininst
python setup.py py2exe
