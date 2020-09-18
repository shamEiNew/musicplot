import spotipy, json, time
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ


def configure():
    cs_id = environ['CLIENT_ID']
    cs_secret = environ['CLIENT_SECRET']

    client_credentials_manager = SpotifyClientCredentials(client_id=cs_id, client_secret=cs_secret)
    return spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def collect_data(sp, name, data, decade, mid, y):
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

def initiate_collection(sp):
    #for i in range(0, len(data)):
    #    print(playlist['tracks']['items'][i]['track']['album']['release_date'][:-6])
    playlist_ids = ['37i9dQZF1DWTJ7xPn4vNaz', '37i9dQZF1DX4UtSsGT1Sbe', '0rZJqZmX61rQ4xMkmEWQar', '5tW8T4fK7DoTtLr8ordLpa','1tPWTwuxOLsE2Do1JQSUxA']
    name = {}
    year = 1970
    mid_year = 1975
    last_year = 1979
    for id in playlist_ids:
        playlist = sp.playlist(playlist_id = id)
        data = playlist['tracks']['items']
        collect_data(sp, name, data, f'{year}s', mid_year, last_year)
        mid_year += 10
        last_year += 10
        year += 10

    data_filtered = json.dumps(name, indent = 4)
    with open("music.json", "w") as outfile: 
        outfile.write(data_filtered)

def albums(sp, artist_ids):
    start_time = time.time()
    final_data = {}
    count_a = 0
    for ids in artist_ids:
        artist_albums = sp.artist_albums(artist_id = ids, album_type='album', country=None, limit=50, offset=0)
        counter = 0
        tracks_ids = []
        data_artists = {}
        albums_list = []
        while artist_albums:
            for _, album in enumerate(artist_albums['items']):
                    counter += 1
                    tracks  = sp.album_tracks(album['id'])
                    while tracks:
                        album_tracks = []
                        for __, track in enumerate(tracks['items']):
                            if track['id'] not in tracks_ids:
                                f = sp.audio_features(track['id'])
                                f = {k:f[0][k] for k in f[0].keys() if k not in ["type","id", "uri", "track_href","analysis_url","duration_ms","time_signature"]}
                                album_tracks.append({'track_name':track['name'],'track_id':track['id'], 'features':[f]})
                                #rint(f"{track['id']} \t {track['name']} \t {track['uri']}")
                        if tracks['next']:
                            tracks = sp.next(tracks)
                        else:
                            albums_list.append({'album_name': album['name'], 'release_date': album['release_date'], 'tracks':album_tracks})
                            tracks = None
        
            if artist_albums['next']:
                artist_albums =  sp.next(artist_albums)
            else:
                artist_albums =  None

        filter_index = []
        albums_list_filtered = []

        for l in range(0, len(albums_list)):
            for m in range(l+1, len(albums_list)):
                    if albums_list[l]['album_name'] == albums_list[m]['album_name']:
                        filter_index.append(l)

        for k in range(0, len(albums_list)):
            if k not in filter_index:
                albums_list_filtered.append(albums_list[k])

        data_artists['artist_name'] = sp.artist(artist_id = ids)['name']
        data_artists['albums_full'] = albums_list_filtered
        final_data[f'artist_{count_a}'] = [data_artists]
        count_a += 1
    
    file_in = json.dumps(final_data, indent = 4)
    with open('music_data/artists_TSKWPF.json', 'w', encoding = 'utf-8') as file_out:
        file_out.write(file_in)

    print(time.time()-start_time)

if __name__ == '__main__':
    #sp = configure()
    #artist_ids = ['5K4W6rqBFWDnAN6FQUkS6x', '06HL4z0CvFAxyc27GXpf02', '0k17h0D3J5VfsdmQ1iZtE9']
    #albums(sp, artist_ids)
    with open('music_data/artists_TSKWPF.json', 'r', encoding= 'utf-8') as f:
       val = json.load(f)

    for key in val.keys():
        for i in val[key]:
            for pee in range(0,len(val[key][0]['albums_full'])):
                print(val[key][0]['albums_full'][pee]['album_name'])