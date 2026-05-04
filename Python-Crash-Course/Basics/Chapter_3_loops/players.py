#Hi i'm shayan and i practice today about looping through a slice
#first i create a list of players and i chose slice first three play with colon (:)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())