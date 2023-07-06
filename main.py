import requests
import spotipy
import os
from bs4 import BeautifulSoup
from spotipy import SpotifyClientCredentials

URL = "https://www.billboard.com/charts/hot-100"
auth_token = ".cache"
songs_list = []
songs_uri = []

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print("Please wait until we retrieve the data. (Do not exit)...")
year = date.split("-")[0]

webpage_link = f"{URL}/{date}/"
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
find_songs = soup.select(selector="li h3", class_="c-title")

for song in find_songs:
    song_text = song.getText()
    song_text = song_text.replace("\n", "").replace("\t", "")
    songs_list.append(song_text)

auth_manager = SpotifyClientCredentials(client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ[
    "SPOTIPY_CLIENT_SECRET"])  # replace SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET with your own. Use them as variables
sp = spotipy.Spotify(auth_manager=auth_manager)

current_user = sp.current_user()["id"]

counter = 0
for song in songs_list:
    my_song = sp.search(q=f"track:{song} year: {year}", limit=1, type="track", market="US")
    try:
        req_uri = my_song["tracks"]["items"][0]["uri"]
    except:
        pass
    else:
        songs_uri.append(req_uri)
    counter += 1
    if counter >= 100:
        break
print(f"Number of songs found: {len(songs_list)} songs")
if len(songs_list) > 100:
    print("We have added the first 100 songs")
new_playlist = sp.user_playlist_create(user=current_user, name=f"{date} Billboard 100", public=False,
                                       collaborative=False,
                                       description=f"Top 100 songs in {year} according to Billboard")
sp.user_playlist_add_tracks(user=current_user, playlist_id=new_playlist["id"], tracks=songs_uri)
print("Playlist created. Enjoy!")
