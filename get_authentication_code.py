import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

my_spotify = spotipy.oauth2.SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    show_dialog=True
)

access_token = my_spotify.get_access_token()

print(sp.current_user()["id"])