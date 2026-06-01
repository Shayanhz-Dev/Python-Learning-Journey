# Practice getting the name of a file or directory from a path using os.path library.
# os.path.basename() function returns the name of the file or directory from a path.
# os.path.dirname() function returns the directory name from a path.
# os.path.splitext() function splits the file name and extension from a path and returns them as a tuple.

import os


path = "E:/Python/Python-Learning-Journey/Python-Libraries/os/checking.py"

print(os.path.basename(path))
print(os.path.dirname(path))

name , ext = os.path.splitext(os.path.basename(path))
print(name)
print(ext)