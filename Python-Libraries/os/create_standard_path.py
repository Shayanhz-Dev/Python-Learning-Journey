# Create a standard path using os.path.join() function.
# This function takes multiple arguments and joins them into a single path,
# using the appropriate separator for the operating system.

import os 

name = "Shayan"
path = os.path.join(
    "users",
    name,
    "images"
)
print(path)