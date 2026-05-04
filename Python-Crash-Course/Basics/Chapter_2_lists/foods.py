#Hi i'm shayan and i want practice today about copying list and create two list with one data and modify each lists 
#First i create one list and one variable and i give variable value of the first list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#Now i have two list i can modify each lists i want
my_foods.append('cannoli')
friend_foods.append('ice cream')
#Now i can Print so easy lists
print(f"My favorite foods are \n {my_foods}")
print(f"My friend favorite foods are \n {friend_foods}")