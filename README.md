## Spotify Playlist Creator 🎵
- - -
This is a python script to retrieve top 100 songs from Billboard and create a playlist and add those songs in your spotify account as a playlist.
### Files Under The Directory
The project includes 2 files.
1. get_authentication_code.py
   1. It is used to generate a ``.cache``file which includes the authentication code required by spotipy to create a playlist in your account.
   2. Run this program if you do not find a ``.cache``file under the root directory of this program to get your own authentication token.
   3. It will redirect you to site which requests authentication. Once done, it will further redirect you to another site.
   4. Copy the link of the redirected site [example.com]("exmple.com")...
   5. Paste it in the console
2. main.py
   1. Once you have your ``auth_token``, you can run the program to create a playlist in your account.
### Before Running The Program
Before running the program, authenticate yourself with Spotify
* [Sign up to Spotify]("http://spotify.com/signup/)
* [Go to the developer dashboard]("https://developer.spotify.com/dashboard/")
* Get your ``Client ID`` and ``Client Secret``

### Walkthrough of the Program
- The program asks you to enter the date in (YYYY-MM-DD) format so that it can retrieve the top 100 songs of the particular time.
- The script uses BeautifulSoup to fetch the top 100 songs from [Billboard]("https://www.billboard.com/charts/hot-100") based on the year the user provided
- A list of top 100 songs is created.
- The program then uses **Spotipy API** to retrieve the uri of each track and return a list of all uris.
- The program authenticates to your spotify account with your permission
- It creates a playlist which includes all the 100 songs retrieved from Billboard.
### Language Used
Python 3.11

### Requirements
If the program doesn't work, make sure to install these-
* Python 3
  * [Install python 3](https://www.python.org/downloads/)
* pip
  * [Install pip](https://pip.pypa.io/en/stable/installation/)
* requests - python package
  * ``pip install requests``
* BeautifulSoup
  * ``pip install bs4``
* spotipy
  * ``pip install spotipy``