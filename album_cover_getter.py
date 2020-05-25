import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

img = sp.album("3prBy9ITryUQUYKuUTn4EM")

print(img)