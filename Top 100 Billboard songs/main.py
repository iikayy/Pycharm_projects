import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Spotify_CLIENT_ID = "ed3fddf8c1934707a5da5fb731d79479"
Spotify_CLIENT_SECRET = "975f69e909d54a07b979b18cb095dc3e"
spotify_USERNAME = "ikay"
URL = "https://www.billboard.com/charts/hot-100/#"

response = requests.get(URL)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
all_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

song_namess = [song.get_text().strip() for song in all_songs]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=Spotify_CLIENT_ID,
        client_secret=Spotify_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=spotify_USERNAME,
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)