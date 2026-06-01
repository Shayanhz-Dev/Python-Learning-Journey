# Practice changing the current working directory using os.chdir() and os.getcwd() functions.
import os

print("Current Directory:", os.getcwd())

target_dir = "C:/Projects"


try:
    os.chdir(target_dir)
    print("New Directory:", os.getcwd())
except FileNotFoundError:
    print(f"Error: The directory '{target_dir}' does not exist.")
