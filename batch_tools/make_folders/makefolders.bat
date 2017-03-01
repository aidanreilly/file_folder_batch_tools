@echo off
for /f "tokens=*" %%a in (folders.txt) do (

mkdir "%%a"

)