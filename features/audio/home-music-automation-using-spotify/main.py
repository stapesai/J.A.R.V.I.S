import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# J.A.R.V.I.S. Credientials
SPOTIPY_CLIENT_ID = '3697ea2b14d84b7eaf1ad8e7205b8bcd'
SPOTIPY_CLIENT_SECRET = '2ed74888a5114b2a84cc121363c6dc49'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))


input_artist = 'spotify:artist:0y59o4v8uw5crbN9M3JiL1'

'''
# Get Artist's all Albums
results = spotify.artist_albums(input_artist, album_type='album')  # all albums of the artist
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])
'''


'''
# Get Artist's 10 Tracks with 30s of  audio preview
results = spotify.artist_top_tracks(input_artist)
for track in results['tracks'][:10]:
    print('track : ' + track['name'])
    print('audio sample : ' + str(track['preview_url']))
    print('cover art : ' + track['album']['images'][0]['url'])
    print()
'''

'''
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Badshah'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
'''