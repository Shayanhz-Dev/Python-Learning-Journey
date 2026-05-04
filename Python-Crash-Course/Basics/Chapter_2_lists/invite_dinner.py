#I'm shayan and i started learn python last night , this is my list training
#I just want use .remove , pop() , del statement , .append and .insert

guests = ['reza', 'mostafa', 'sara', 'negin']
print(f"Hello {guests[0].title()} i want invite you for dinner to night")
print(f"Hello {guests[1].title()} i want invite you for dinner to night")
print(f"Hello {guests[2].title()} i want invite you for dinner to night")
print(f"Hello {guests[3].title()} i want invite you for dinner to night")
#Now i use pop() for sara and .insert for fayaz
print(f"I heard that one of my guests cant make the dinner, so i replace him and send new message to another guests")
popped_guest = guests.pop(2)
new_guest = guests.insert(2, 'fayaz')
print(f"Hello my friends i talk to {popped_guest.title()} and she say cant come for dinner to night so i want invite another person for the dinner to night he is {guests[2].title()}")
print(f"\n\t new list guests is {guests}")
#Now i found i bigger table and i want invite more guests to night
guests.insert(0, "hanie")
guests.insert(3, "mahdis")
guests.append("mehdi")
print(f"\nNew list guests for new table is {guests}")
#my table wont arrive in time for the dinner, and now  i have space for only two guests
print(f"I'm sorry my friend becouse my table wont arrive in time for the dinner, and now  i have space for only two guests")
hanie = guests.pop(0)
mahdis = guests.pop(2)
fayaz = guests.pop(2)
negin = guests.pop(2)
mehdi = guests.pop(2)
print(f"I'm realy sorry my friends {hanie.title()} becouse i only have two space for guests , i invite you later goodbye")
print(f"I'm realy sorry my friends {mahdis.title()} becouse i only have two space for guests , i invite you later goodbye")
print(f"I'm realy sorry my friends {negin.title()} becouse i only have two space for guests , i invite you later goodbye")
print(f"I'm realy sorry my friends {fayaz.title()} becouse i only have two space for guests , i invite you later goodbye")
print(f"I'm realy sorry my friends {mehdi.title()} becouse i only have two space for guests , i invite you later goodbye")
#Now i send message to two guests still invited to night
print(f"Hello {guests[0].title()} and {guests[1].title()} i have two space to night for dinner and you are in my guests list i see you to night")
#ohhh i dont have food for to night
del guests[0]
del guests[0]
print(guests)
print("I have sleep to night with peace")
print(len(guests))
