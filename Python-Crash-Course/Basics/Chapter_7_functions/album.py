# Hi I'm shayan and today I want to practice function
# 1. Create function with prarameters 
# 2. Create a dictionary with key-parameters(values)
# 3. Use if statement for checking Tracks parameter is not none and add key-values
# 4. Return dictionary
# 5. Positional Calls function
def make_album(artis_name, album_title, tracks=None):
    """Display informations of album"""
    album = {'artis': artis_name, 'title': album_title}
    if tracks is not None:
        album['tracks'] = tracks
    return album
print(make_album('godmehr', 'goli', '21'))
print(make_album('shayan', 'rise', '7'))
print(make_album('mahdi', 'dezho'))