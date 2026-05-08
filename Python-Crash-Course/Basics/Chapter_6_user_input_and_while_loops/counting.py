# Hi I'm shayan and today I want to practice while-loop
# 1. Create a variable with value
# 2. Create a while-loop with Boolean expression
# 3. Add 1 to the number each time the loop repeats
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

# modified code:
# using continue for rest loop in next number
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    