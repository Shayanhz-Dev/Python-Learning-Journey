# Practice creating a new folder using os.mkdir() function

import os


os.mkdir("NewFolder") # Only creates one folder at a time
os.makedirs("data/images/users", exist_ok=True) # Creates multiple folders at once. 
os.rmdir("NewFolder") # Deletes an empty folder
os.removedirs("data/images/users") # Deletes multiple folders at once. Only deletes empty
files_list = os.listdir()

print(files_list)