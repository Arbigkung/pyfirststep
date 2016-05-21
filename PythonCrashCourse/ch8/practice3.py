#City name

def city_country(city, country):
    result = city + ", " + country
    return result    

ex1 = city_country('Santiago', 'Chile')
print(ex1)

# Album

def make_album(artist_name, album_title, num_track=''):
    album = {artist_name : album_title}
    
    if num_track:
        album['number of track'] = num_track
        
    return album

print(make_album('big', 'we go for a dream', 20))

# Album again with while loop
while True:
    print('\nplease enter artist, and album title')
    print('(type q to exit any time)')
    
    name = raw_input('name of the artist: ')
    if name == 'q':
        break
    
    title = raw_input('title of album: ')
    if title == 'q':
        break
    
    result = make_album(name, title)
    print(result)
