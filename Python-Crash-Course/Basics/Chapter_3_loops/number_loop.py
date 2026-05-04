#Hello i'm shayan and i want to practice today numerical loop list in the Python
#First i build a easy list loop 1-20
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
#Now i want to create a list comprehension with one million number and perform operations on the list
#First i create a variable for list comprehension
#Now i use min - max - sum on my list numbers
millions = [million for million in range(1, 1000001)]
print(millions)
print(min(millions))
print(max(millions))
print(sum(millions))
#in the next step i want create a loop with odd numbers i use "2 step" on loop range for odd number
odd_numbers = [odd_number for odd_number in range(1, 20, 2)]
print(odd_numbers)
#My next step is multiples of 3 
threes = [three for three in range(3, 31, 3)]
print(threes)
#i want create new loop list for make number to cube and print each time number added list
cubes = []
for number in range(11):
    cube = number**3
    cubes.append(cube)
    print(cubes)
#Now i want create a cube comprehension 
#i create list and loop in one line
cubes_comprehension = [new_cube**3 for new_cube in range(11)]
print(cubes_comprehension)