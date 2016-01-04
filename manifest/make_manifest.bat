SET output=manifest.xml
ECHO ^<manifest sourcepath="%~dp0"^> > %output%
FOR %%f in ("*.dita") DO (
    ECHO      ^<file href="%%~nf.dita"/^> >> %output%
)
ECHO ^</manifest^> >> %output%