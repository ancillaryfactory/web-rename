WebRename version 0.3

http://ancillaryfactory.github.com/web-rename/
========================================================================

INSTALLATION:
Run setup.bat to copy webname.exe to C:\Convert to slug

If necessary, create the following registry keys:
HKCR\*\shell\Convert filename to slug
HKCR\*\shell\Convert filename to slug\command" /d "C:\Convert to slug\webname.exe "%1"



USAGE
1. Right-click a file in Windows Explorer and select "Rename for Web"
2. Drag a file to webname.exe

In both cases, spaces in the filename will be converted to hyphens.


======================================================

Windows .EXE compiled with PyInstaller (http://www.pyinstaller.org)