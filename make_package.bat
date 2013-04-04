rem create .html from README files
rst2html.py README > README.html

rem create python package
python setup.py sdist --formats=zip,gztar
python setup.py bdist_wininst
python setup.py py2exe
