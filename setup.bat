mkdir "c:\Program Files\Convert to slug"
copy "webname.exe" "c:\Program Files\Convert to slug"
copy "setup.bat" "c:\Program Files\Convert to slug"
copy "uninstall.bat" "c:\Program Files\Convert to slug"
copy "readme.txt" "c:\Program Files\Convert to slug"


REG ADD "HKCR\*\shell\Convert filename to slug"
REG ADD "HKCR\*\shell\Convert filename to slug\command" /d "C:\Program Files\Convert to slug\webname.exe \"%%1\""

echo msgbox"All done. Try right-click->Convert filename to slug">a.vbs&a.vbs
DEL /F /S /Q /A "C:\Program Files\Convert to slug\a.vbs"
cls