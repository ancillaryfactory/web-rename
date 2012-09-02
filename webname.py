import sys
import os
import re


full_path = os.path.split(sys.argv[1]) 
origin = full_path[0]
name = full_path[1]
 
# Thanks to http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
fixed_name = re.sub(r'\W+', '-', name)
fixed_path = os.path.join(origin, fixed_name)

# convert tuple to string
fixed_path_string = ''.join(fixed_path)

os.rename(sys.argv[1], fixed_path_string) 