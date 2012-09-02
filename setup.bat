mkdir "c:\Program Files\webname"
copy "webname.exe" "c:\Program Files\webname"

REG ADD "HKCR\*\shell\Rename for Web"
REG ADD "HKCR\*\shell\Rename for Web\command" /d "C:\Program Files\webname\webname.exe \"%%1\""