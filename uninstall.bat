DEL /F /S /Q /A "C:Convert to slug\*"
RMDIR "C:\Convert to slug"

REG DELETE "HKCR\*\shell\Convert filename to slug" /f