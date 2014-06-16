#!/usr/bin/env python
"""get version of suzu"""

import os

ver_file = os.path.join(os.path.dirname(__file__), '..', 'suzu', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

print(vars['__version__'])

# to environment variable in cmd.exe
# for /f usebackq %%1 in (`python suzu_version.py`) do (@set VAR=%%1)
