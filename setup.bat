mkdir "c:\Program Files\Webname"
copy "webname.exe" "c:\Program Files\Webname"

REG ADD "HKCR\*\shell\Rename for Web"
REG ADD "HKCR\*\shell\Rename for Web\command" /d "C:\Program Files\Webname\webname.exe \"%%1\""