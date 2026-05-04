#Hello my name is shayan and this is my training case about loop in Python 
#I just want use 'for' loop in any list and print a message this is my practice
#I create one variable (pizzas) but i use pizza in print because pizza is in my loop name for pizzas
#I use colon (:) because i want tell Python  to interpret the next line as the start of a loop
pizzas = ['pepperoni', 'margherita', 'hawaiian']
pizzas.append("chicken")
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!\n")
#I print a message outside loop for Indentation rules
print("\t\nI really like pizzas, pizza is not food, pizza is a lifestyle")
#Today i want modify pizza code with copying list and add item in list
friend_pizzas = pizzas[:]
friend_pizzas.append("special")
for friend_pizza in friend_pizzas:
    print(f"my friend's favorite pizza is{friend_pizza.title()}\n")