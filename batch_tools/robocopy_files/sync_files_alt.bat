@echo off
set source="C:\SVN\simplex_datasheets"
set destination="\\uswmi3ap00004\TechnicalPublications$\Data_Sheet_Backup\Simplex_DS"

::Not sure if this is needed
::It guarantees you have a canonical path (standard form)
for %%F in (%destination%) do set destination="%%~fF"

for /r %source% %%F in (.) do if "%%~fF" neq %destination% ROBOCOPY "%%F" %destination% *.doc sync_westminster_log.txt /R:0 /LOG:sync_westminster_log.txt
