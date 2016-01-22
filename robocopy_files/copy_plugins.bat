set plugins_folder="C:\Program Files\Oxygen XML Editor 17\frameworks\dita\DITA-OT2.x\plugins"

Robocopy %~d0 %plugins_folder% /S /E /xf copy_plugins.bat /xf readme.txt
