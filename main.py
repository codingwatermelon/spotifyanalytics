# Spotipy library reference https://spotipy.readthedocs.io/en/2.19.0/
# See 'authorization code flow' section, export relevant env variables

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

def get_user_library(scope):
    client_id = os.environ.get('spotify_client_id')
    client_secret = os.environ.get('spotify_client_secret')
    client_redirect_uri = os.environ.get('spotify_client_redirect_uri')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    results = sp.current_user_saved_tracks(limit=30, offset=2)
    for idx, item in enumerate(results['items']):
        track = item['track']
        #print(idx, track['artists'][0]['name'], " – ", track['name'])
        print(idx, track['artists'][0]['name'], "test ", track['name'])

def get_currently_playing(scope):
    client_id = os.environ.get('spotify_client_id')
    client_secret = os.environ.get('spotify_client_secret')
    client_redirect_uri = os.environ.get('spotify_client_redirect_uri')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    print(sp.currently_playing())

def get_user_top(scope):
    client_id = os.environ.get('spotify_client_id')
    client_secret = os.environ.get('spotify_client_secret')
    client_redirect_uri = os.environ.get('spotify_client_redirect_uri')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    print(sp.current_user_top_artists(time_range='short_term', limit=50))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scope = "user-library-read"
    #scope = "user-read-currently-playing"

    #scope = "user-top-read"

    get_user_library(scope)
    #get_currently_playing(scope)
    #get_user_top(scope)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
