# Practice: Checking if a path is a file or directory using os.path library.
import os


# Checks if a path is a directory. Returns True if it is, otherwise False.
print(os.path.isdir("images"))

# Checks if a path is a file. Returns True if it is, otherwise False.
print(os.path.isfile("data.txt"))

# Checks if a file or directory exists. Returns True if it exists, otherwise False.
print(os.path.exists("data.txt"))
