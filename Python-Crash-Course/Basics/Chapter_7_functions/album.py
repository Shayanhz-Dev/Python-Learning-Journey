# Hi I'm shayan and today I want to practice function
# 1. Create function with parameters 
# 2. Create a dictionary with key-parameters(values)
# 3. Use if statement for checking Tracks parameter is not none and add key-values
# 4. Return dictionary
# 5. Positional Calls function
# Modified code
# 1. Create a empty list for save user-inputs
# 2. Create while-loop-infinite for getting userinputs
# 3. Create if statement to checking user-inputs is correct
# 4. Call function with user-inputs(arguments) in if statement
# 5. Add user-inputs to list
# 6. Use for-loops for Print list-items
def make_album(artist_name, album_title, tracks=None):

    """Display information of album"""
    album = {'artist': artist_name, 'title': album_title}
    if tracks is not None:
        album['tracks'] = tracks
    return album

albums_list = []

while True:
    print("\nEnter your favorite album information")
    print("(Enter 'quit' to exit program)")
    artist = input("Artist name: ").lower().strip()
    if artist == 'quit':
        break

    title_album = input("Album title: ").lower().strip()
    if title_album == 'quit':
        break

    tracks = input("Tracks: ").strip()
    if tracks == 'quit':
        break
    if not tracks:
        user_album = make_album(artist, title_album)
        print(user_album)
        
    elif not tracks.isdigit():
        print("Please enter a valid number!")
        continue
    else:
        user_album = make_album(artist, title_album, int(tracks))
        print(user_album)
    albums_list.append(user_album)

print("\nUser Favorite albums")

for album in albums_list:
    print(album)

print("\n\t(My program default albums)")
print(f"\t{make_album('godmehr', 'goli', 21)}")
print(f"\t{make_album('shayan', 'rise', 7)}")
print(f"\t{make_album('mahdi', 'dezho')}")