mkdir "c:\Convert to slug"
copy "webname.exe" "c:\Convert to slug"
copy "setup.bat" "c:\Convert to slug"
copy "uninstall.bat" "c:\Convert to slug"
copy "readme.txt" "c:\Convert to slug"


REG ADD "HKCR\*\shell\Convert filename to slug"
REG ADD "HKCR\*\shell\Convert filename to slug\command" /d "C:\Convert to slug\webname.exe \"%%1\""

echo msgbox"All done. Try right-click->Convert filename to slug">a.vbs&a.vbs
DEL /F /S /Q /A "a.vbs"
cls