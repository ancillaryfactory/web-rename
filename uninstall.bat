DEL /F /S /Q /A "C:\Program Files\Convert to slug\*"
RMDIR "C:\Program Files\Convert to slug"

REG DELETE "HKCR\*\shell\Convert filename to slug" /f