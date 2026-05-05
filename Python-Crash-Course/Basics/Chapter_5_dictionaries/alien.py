#Hi I'm shayan and today i want to practice about dictionaries and learn about it
#First i create a dictionarie with key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#second I want adding new key-value pairs in my dictionary 

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Third I want start with empty dicstionary
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 15
print(alien_0)

#fourth I want modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#Now I want to remove key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)