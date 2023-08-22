from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"

artist = sys.argv[1]
track = sys.argv[2]

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
track_id = sp.search(q=f"{artist} {track}", type='track', limit=1)
single_url = f"{track_id['tracks']['items'][0]['external_urls']['spotify']}"
track_id = single_url.split("/")[-1]
print(track_id)
