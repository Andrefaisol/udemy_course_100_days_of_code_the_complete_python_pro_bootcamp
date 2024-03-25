from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

APP_CLIENT_ID = "" # insert your spotify client ID
APP_CLIENT_SECRET = "" # insert your spotify client secret ID
APP_REDIRECT_URI = "https://example.org/callback"
date = input("Which year do you want to back? type the date in this format YYYY-MM-DD: ")
list_date = date.split("-")
while (list_date[0].isalpha() or list_date[1].isalpha() or list_date[2].isalpha() or len(list_date[0]) > 4 or
       len(list_date[1]) > 2) or len(list_date[2]) > 2:
    date = input("Which year do you want to back? type the date in this format YYYY-MM-DD: ")
    list_date = date.split("-")

titles_list = []
singer_list = []
URL = f"https://www.billboard.com/charts/hot-100/{date}"
data_for_scrap = requests.get(url=URL).text
soup = BeautifulSoup(data_for_scrap, "html.parser")
tag = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
                                      "lrv-u-flex-direction-column "
                                      "lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max "
                                      "lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
song_list = [song.getText() for song in tag]
replaced = [i.replace("\t", "") for i in song_list]
splited = [i.split("\n") for i in replaced]

singer = soup.find("div", class_="lrv-u-flex u-align-items-center@mobile-max")

num1 = [label.getText() for label in singer]
replaced_num1 = [i.replace("\t", "") for i in num1]
splited_num1 = replaced_num1[3].split("\n")
song_num1 = splited_num1[5]
singer_num1 = splited_num1[8]

titles_list.append(song_num1)
for i in splited:
    titles_list.append(i[6])

singer_list.append(singer_num1)
for i in splited:
    singer_list.append(i[11])


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                                               client_secret=APP_CLIENT_SECRET,
                                               scope="playlist-modify-private playlist-modify-public",
                                               redirect_uri=APP_REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=""))
# insert username with your spotify username
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in titles_list[0:10]:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"Billboard top songs with Python"
playlist_description = "Created with Python"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
