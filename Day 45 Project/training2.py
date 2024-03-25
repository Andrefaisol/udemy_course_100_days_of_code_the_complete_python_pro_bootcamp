from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
y_combinator_news = response.text

soup = BeautifulSoup(y_combinator_news, "html.parser")
article_tag = soup.find_all(name="span", class_="titleline")
article_txt = []
article_links = []
for article in article_tag:
    text = article.getText()
    article_txt.append(text)
    link = article.select("a")[0].get("href")
    article_links.append(link)

upvote = soup.find_all(name="span", class_="score")
upvote_list = [int(vote.getText().split()[0]) for vote in upvote]


highest_upvote_index = upvote_list.index(max(upvote_list))
print(article_txt[highest_upvote_index])
print(article_links[highest_upvote_index])
print(upvote_list[highest_upvote_index])

