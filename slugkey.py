import sys
import os
import re

import pyhk
import time,win32api,win32con,win32gui
from win32clipboard import *



def slugify_clipboard_string():
	# http://stackoverflow.com/questions/3827511/copying-and-pasting-from-to-clipboard-with-python-win32
	OpenClipboard() 
	contents = GetClipboardData(win32con.CF_TEXT) # get clipboard data

	# fix the contents here
	fixed_name = re.sub(r'\W+', '-', contents)
	
	# put the fixed string back on the clipboard
	EmptyClipboard()
	SetClipboardData(win32con.CF_TEXT, fixed_name)
	CloseClipboard()

	# paste the clipboard
	# http://code.activestate.com/lists/python-list/584186/
	# win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
	# win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
	# time.sleep(0.05)
	# win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
	# win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

	del fixed_name, contents


#create pyhk class instance
hot = pyhk.pyhk()
 
#add hotkey
hot.addHotkey(['Ctrl','Alt','G'],slugify_clipboard_string)
 
#start looking for hotkey.
hot.start()