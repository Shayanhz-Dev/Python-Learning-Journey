#Hi i'm Shayan and today I want to practice if statement with series of conditional test 
#First I create a variable and i make True and False questions for checking equality and inequality of variable value
game = "Valorant"
print("Is game == 'Valorant' ? i predict True.")
print(game == "Valorant")

print("\nIs game =='apex'? I predict False.")
print(game == "apex")

print("\nIs not game == 'fortnite'? I predict True.")
print(game != "fortnite")

print("\nIS not game =='counter strike'? I predict True.")
print(game != "counter strike")

print("\nIs game == 'Valorant'? I predict True.")
print(game.lower() == "valorant")
#second I want to use if statement for a variable inequality
print("\nThis game is minecraft?")
if game != "minecraft":
    print("True")
else:
    print("False")
#Third I create a list (game_list) and make a loop for if statement check each game in my list
print("\nWhich game in list is 'Valorant'?\n")
game_list = ['Minecraft', 'battlefield', 'apex legend', 'valorant']
for game_select in game_list:
    if game_select == "valorant":
        print(f"\n\tThis is {game_select.title()}")
    else:
        print(f"\tThis game is {game_select.title()},is not 'Valorant'")
#Fourth I create a new variable and check my variable in game_list 
#if statement checking inequality my variable value inequality
my_game = 'valorant'
if my_game not in game_list:
    print(f"\nDelete the Games! I want play {my_game.title()}")
else:
    print(f"\nI can play now {my_game.title()}\n")
#Now I want to create numbrical test 
#First I create list of numbers (my_numbers)
#I make a loop for number and if statement for checking value with >= or =<
my_numbers = [18, 15, 20, 21, 23, 24, 25]
for number in my_numbers:
    if number > 19:
        print(f"\t{number}, is bigger than 19")
    else:
        print(f"\t{number}, is lower than or equal to 19")
#second numrical practice I want to use slice of list for my if statement
print("\nChecking first three number in list is 21\n")
for numbers in my_numbers[:4]:
    if numbers != 21:
        print(f"\t{numbers}, is not my number")
    else:
        print(f"\n\t{numbers}, this is my number!")
#Third I want use "or" and "and" in if statement
print("\nlets checking numbers without loop!")
if 21 in my_numbers and 22 in my_numbers:
    print("\t21 and 22 are BOTH in my list")
else:
    print("\t21 and 22 are NOT both in my list")

if 18 in my_numbers or 19 in my_numbers:
    print("\t18 or 19 is in my list!")
else:
    print("\t18 or 19 is not in my list!")
