WebRename version 0.2

Add 'Rename for Web' to the Context Menu
===============================================================

\HKEY_CLASSES_ROOT\*\shell -> create key named 'Rename for web'

Create subkey named 'command'

Double-click 'default' in right pane

Set value to C:\path\to\file\webname.exe "%1"


======================================================

Windows .EXE compiled with PyInstaller (http://www.pyinstaller.org)