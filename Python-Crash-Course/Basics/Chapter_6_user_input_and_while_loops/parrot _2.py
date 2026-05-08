# Hi I'm shayan and today I want to start chapter_6 - user input and while loops
# 1. This is parrot file new version
# 2. I just want to use a flag

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)