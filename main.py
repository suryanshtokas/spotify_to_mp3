from spotify import Spotify

spotify_api = Spotify()
songs_list = spotify_api.get_playlist_songs("1w42XRhVieJiqZjXafXaY5?si=572e402bf75442df")

print(songs_list)
