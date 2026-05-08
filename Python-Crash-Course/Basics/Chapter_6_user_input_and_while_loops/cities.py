# Hi I'm shayan and today I want practice to input getting user
# 1. Create a while-loop
# 2. Using Break for exiting loop

prompt  = "\nPlease enter the name of a city you have visited: "
prompt  += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt )

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")