from bs4 import BeautifulSoup
import lxml
with open(file="website.html", encoding="utf8") as data:
    contents = data.read()

soup = BeautifulSoup(contents, 'lxml')

print(soup.title.string)
all_anchors = soup.find_all(name="a")
print(all_anchors)

for tag in all_anchors:
    print(tag.get("href"))
