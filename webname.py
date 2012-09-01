import sys
import os


full_path = os.path.split(sys.argv[1]) 
origin = full_path[0]
name = full_path[1]
 
# build new filename here
fixed_name = name.replace(' ', '-')
fixed_path = os.path.join(origin, fixed_name)

# convert tuple to string
fixed_path_string = ''.join(fixed_path)

os.rename(sys.argv[1], fixed_path_string) 