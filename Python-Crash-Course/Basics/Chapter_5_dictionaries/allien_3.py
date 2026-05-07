# Hi I'm shayan and today I want to practice dictionary , list and managing items
# 1. I create three dictionaries and assign in list 
# 2. I use for-loop for print each item in my list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
# 1. Create empty list
# 2. Create for loop
# 3. Create 30 alien with for-loop
# 4. Create new variable and assign dictionary value in variable
# 5. Append dictionary variable in aliens list
# 6. Print each value in list with for-loop
# 7. Print total number value in my aliens list
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Modify code:
# I want change first three aliens 
# 1. Create for-loop in slice of list
# 2. Make if statement to check alien status and change it

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens:
    print(alien)
print(".....")
print(f"total number of aliens: {len(aliens)}")