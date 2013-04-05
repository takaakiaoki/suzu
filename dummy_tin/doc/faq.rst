=============
FAQs
=============

Invoke TRIM.exe from suzu
=========================

SUZU invokes trim.exe when these two conditions are satisfied.

- Save data with the filename of 'TRIM.in' 

- TRIM.exe exists in the same folder where new TRIM.in is saved.

User Profile
============

In usual, use profile data is saved in C:\\Users\\(username)\\AppData\\Roaming\\suzu

SUZU searches user profile data in this order. (%VALUE% means system environment variable)

1. %SUZUPROFILEDIR%
2. %APPDATA%\\suzu  (windows only)
3. %HOME%\\.suzu
