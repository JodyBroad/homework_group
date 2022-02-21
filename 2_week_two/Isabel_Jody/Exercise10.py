# Shared file with Isabel & Jody - Exercise 10

import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# Search functionality, I am looking for files in this format
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
for name in glob.glob(pattern):
    print(name)

# TODO: use os.path.getsize to find each file's size
# for name in glob.glob(pattern):
#    print(os.path.getsize(name))

# TODO: Add a test to only display files that are not zero length
print("All files that are not 0 length are:")
for name in glob.glob(pattern):
    size = os.path.getsize(name)
    if size > 0:
        print(os.path.getsize(name), os.path.basename(name))

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
#print(os.path.basename(name))
