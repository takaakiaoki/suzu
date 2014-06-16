for %%i in (*.rst) do (if %%~xi==.rst rst2html.py %%i %%~ni.html)
