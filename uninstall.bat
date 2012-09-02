DEL /F /S /Q /A "C:\Program Files\Webname\*"
RMDIR "C:\Program Files\Webname"

REG DELETE "HKCR\*\shell\Rename for Web" /f

echo msgbox"Rename for Web uninstalled.">a.vbs&a.vbs