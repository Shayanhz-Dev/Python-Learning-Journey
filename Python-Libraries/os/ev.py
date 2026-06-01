# This code demonstrates how to access environment variables in Python using the `os` module.

import os

user = os.getenv("USERNAME") 
path = os.getenv("PATH")
API_KEY = os.getenv("API_KEY")

print(user)
print(path)
print(API_KEY)