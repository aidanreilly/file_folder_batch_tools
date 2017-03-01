/*merges pdfs in the folder in which the file resides*/
@echo off
setlocal enabledelayedexpansion
FOR %%A IN (%*) DO (set command=!command! %%A)
pdftk.exe %command% cat output "%~dp1binder.pdf"