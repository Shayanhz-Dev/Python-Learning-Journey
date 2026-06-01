# practice os.listdir() function to list all files and directories in the current working directory.

import os


# List files
files = os.listdir()
print("Current directory contents:", files)

# Remove a file safely
file_to_remove = "test.txt"
if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"Deleted {file_to_remove}")
else:
    print(f"File '{file_to_remove}' not found.")

# Rename a file safely
old_name, new_name = "old.txt", "new.txt"
try:
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}")
except FileNotFoundError:
    print(f"File '{old_name}' not found to rename.")
