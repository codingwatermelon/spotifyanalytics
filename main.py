# Spotipy library reference https://spotipy.readthedocs.io/en/2.19.0/
# See 'authorization code flow' section, export relevant env variables

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import spotipy
import os
import time
import datetime
from spotipy.oauth2 import SpotifyOAuth

def get_user_library(scope, output):

    client_id = os.environ.get('spotify_client_id')
    client_secret = os.environ.get('spotify_client_secret')
    client_redirect_uri = os.environ.get('spotify_client_redirect_uri')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    results = sp.current_user_saved_tracks(limit=50, offset=0)
   
    f = open(output, "a")
    
    i=0
    done = False
    while not done:
    
            for idx, item in enumerate(results['items']):
                track = item['track']
                #print(idx, track['artists'][0]['name'], " – ", track['name'])
                string="{} {} - {}".format(idx+i+1, track['artists'][0]['name'], track['name'])
                #print(idx+i+1, track['artists'][0]['name'], "-", track['name'])
                print(string)
                f.write(string+"\n")
         
            if len(results['items']) < 50:
                done = True

            else:
                i+=50
                results = sp.current_user_saved_tracks(limit=50, offset=i)
            
            time.sleep(0.25)

    f.close()

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
    date = datetime.datetime.now()

    scope = "user-library-read"
    #scope = "user-read-currently-playing"

    #scope = "user-top-read"
    output= "/home/pi/spotipy/spotifyanalytics/allsongs_{}.txt".format(date.strftime("%Y_%m_%d"))
    get_user_library(scope, output)
    #get_currently_playing(scope)
    #get_user_top(scope)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
