# Spotipy library reference https://spotipy.readthedocs.io/en/2.19.0/

# Notes:
# - Upon first execution, API will ask for authorization via web browser redirect URI. Paste the redirect site, then it will generate a .cache file so you don't have to do it again.

import spotipy
import time
import datetime
import json
from spotipy.oauth2 import SpotifyOAuth

def get_vars():
    data = json.load(open('config.json'))

    return data['spotify_client_id'], data['spotify_client_secret'], data['spotify_client_redirect_uri']

def get_user_library(scope, output):

    client_id, client_secret, client_redirect_uri = get_vars()

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    results = sp.current_user_saved_tracks(limit=50, offset=0)
   
    f = open(output, "a", encoding="utf-8")
    
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
            
            # Add sleeps to throttle API requests (Spotify will get mad at me if not)
            time.sleep(0.25)

    f.close()

def get_currently_playing(scope):
    client_id, client_secret, client_redirect_uri = get_vars()

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    print(sp.currently_playing())

def get_user_top(scope):
    client_id, client_secret, client_redirect_uri = get_vars()

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_uri))

    print(sp.current_user_top_artists(time_range='short_term', limit=50))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    date = datetime.datetime.now()
    #scope = "user-read-currently-playing"

    #scope = "user-top-read"

    # where scope is "user-library-read"
    get_user_library("user-library-read", "allsongs_{}.txt".format(date.strftime("%Y_%m_%d")))

    #get_currently_playing(scope)
    #get_user_top(scope)
