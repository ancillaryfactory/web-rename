Add 'Rename for Web' to the Context Menu
===============================================================

\HKEY_CLASSES_ROOT\*\shell -> create key named 'Rename for web'

Create subkey named 'command'

Double-click 'default' in right pane

Set value to C:\path\to\file\webname.exe "%1"