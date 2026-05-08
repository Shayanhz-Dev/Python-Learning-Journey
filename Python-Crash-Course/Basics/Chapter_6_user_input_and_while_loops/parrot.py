# Hi I'm shayan and today I want to start chapter_6 - user input and while loops
# 1. input practice 

message = input("Tell me something, and I will repeat it back to you:")
print(message)

# Modified code:
# 2. Create variable for message
# 3. Create new variable for checking with while-loop
# 4. Create while-loop with != 'quit'
# 5. Add user input to first variable
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = "\t"
while message != 'quit':
    message = input(prompt)
    if message != "quit":
         print(message)  