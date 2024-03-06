from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find(name="a", rel="noreferrer")
text = article_tag.string # or article_tag.getText()
link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").get_text()

articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.string # or article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

max_num = max(article_upvote)
max_index = article_upvote.index(max_num)
print(article_texts[max_index])
print(article_links[max_index])










# import lxml
#
# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
#     # print(tag.get_text())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(".heading")
# print(headings)