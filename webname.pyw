import sys
import os
import re
from Tkinter import Tk



def copy_to_clipboard(fixed_name):
	# add new filename to clipboard
	# http://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(fixed_name)
	r.destroy()


def slugify_full_path(full_path):
	# full_path = os.path.split(sys.argv[1]) 
	origin = full_path[0]
	name = full_path[1]

	# split original filename into name and extension
	name_and_extension = os.path.splitext(name)
	name_only = name_and_extension[0]
	extension = name_and_extension[1]

	# Thanks to http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
	fixed_name = re.sub(r'\W+', '-', name_only) + extension
	fixed_path = os.path.join(origin, fixed_name)

	# convert tuple to string
	fixed_path_string = ''.join(fixed_path)

	os.rename(sys.argv[1], fixed_path_string) 
	copy_to_clipboard(fixed_name)


slugify_full_path(os.path.split(sys.argv[1]))





