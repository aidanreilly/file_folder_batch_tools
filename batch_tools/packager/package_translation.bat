set SAVESTAMP=%DATE:/=_%

7z a -tzip %SAVESTAMP%_translation.zip @list.txt
