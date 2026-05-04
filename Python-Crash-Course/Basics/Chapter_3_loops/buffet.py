#Hi my name is shayan and today i want practice tuple and writing over tules loop
#First i create one tuple and loop for menu restaurant , i print menu
food_menu = ("pizza", "burger", "pasta", "salad", "steak")
for food in food_menu:
    print(food.title())
#Now i want change two item i cant change tupple but i can remake variable food_menu for new items

food_menu = ("pepperoni" ,"chicken burger", "pasta", "salad", "steak")
print("\nNew Menu items:")
for food in food_menu:
    print(food.title())