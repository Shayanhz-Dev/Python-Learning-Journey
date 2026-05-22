# Hi I'm shayan and today I want to practice files and exceptions 
# Create a file reader 

from pathlib import Path

path = Path("E:/python/Python-Learning-Journey/Python-Crash-Course/Basics/Chapter_9_file_and_exceptions/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
