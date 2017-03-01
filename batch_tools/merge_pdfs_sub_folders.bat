@Echo Off & SetLocal EnableExtensions
rem Setting Environment
rem This requires PDFtk to be installed

for %%* in (.) do set CurrentDirName=%%~nx*
echo %CurrentDirName%

Set "PDFParent=%~dp0"
Set "PDFMerged=%CurrentDirName%.pdf"
Set "PDFListed="

Rem Listing PDFs for catenation
PushD %PDFParent%||GoTo :EOF
For /D %%A In (*) Do (For %%B In ("%%A\*.pdf") Do (If Not Defined PDFListed (
   Set PDFListed="%%~B") Else (Call Set PDFListed=%%PDFListed%% "%%~B")))

Rem Catenating PDFs
If Defined PDFListed (
   For %%A In ("%PDFMerged%") Do If Not Exist "%%~dpA" (MD "%%~dpA"||GoTo :EOF)
   PDFtk %PDFListed% output "%PDFMerged%")