import requests
from bs4 import BeautifulSoup
import html
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
data_for_scrap = requests.get(url=URL).text
soup = BeautifulSoup(data_for_scrap, "html.parser")
tag = soup.find_all("h3", class_="title")
movie_list = [movie.getText() for movie in tag]
reverse_list = movie_list[::-1]


with open(file="movie_list.txt", mode="w", encoding="utf8") as file:
    for i in reverse_list:
        file.write(f"{i}\n")
