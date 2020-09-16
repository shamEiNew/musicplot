import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ
import json

def configure():
    cs_id = environ['CLIENT_ID']
    cs_secret = environ['CLIENT_SECRET']

    client_credentials_manager = SpotifyClientCredentials(client_id=cs_id, client_secret=cs_secret)
    return spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def collect_data(decade,mid, y):
    l = []
    for i in range(0, len(data)):
        s = []
        songs_temp = {}
        t = {}
        m =[]
        if not data[i]['track']['album']['release_date'][:-6] or int(data[i]['track']['album']['release_date'][:-6]) > y: t['year'] = mid
        else:t['year'] = int(data[i]['track']['album']['release_date'][:-6])
        t['id'] = data[i]['track']['id']
        songs_temp['track_name'] = data[i]['track']['name']
        t['duration'] = data[i]['track']['duration_ms']
        f = sp.audio_features(data[i]['track']['id'])
        f = {k:f[0][k] for k in f[0].keys() if k not in ["type","id", "uri", "track_href","analysis_url","duration_ms","time_signature"]}
        t['properties'] = f
        s.append(t)
        songs_temp['features'] = s
        m.append(songs_temp)
        l.append({f'track_{i}': m})

    name[decade]=l

#for n in name:
#    print(f"{n}\t{urls[name.index(n)]}\t{music_id[name.index(n)]}")
if __name__ == '__main__':
    #for i in range(0, len(data)):
    #    print(playlist['tracks']['items'][i]['track']['album']['release_date'][:-6])
    sp = configure()
    playlist_ids = ['37i9dQZF1DWTJ7xPn4vNaz', '37i9dQZF1DX4UtSsGT1Sbe', '0rZJqZmX61rQ4xMkmEWQar', '5tW8T4fK7DoTtLr8ordLpa','1tPWTwuxOLsE2Do1JQSUxA']
    name = {}
    year = 1970
    mid_year = 1975
    last_year = 1979
    for id in playlist_ids:
        playlist = sp.playlist(playlist_id = id)
        data = playlist['tracks']['items']
        collect_data(f'{year}s', mid_year, last_year)
        mid_year += 10
        last_year += 10
        year += 10

    data_filtered = json.dumps(name, indent = 4)
    with open("music.json", "w") as outfile: 
        outfile.write(data_filtered) 