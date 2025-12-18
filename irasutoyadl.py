import requests
from bs4 import BeautifulSoup
from pathlib import Path


load_url = "https://www.irasutoya.com/2020/09/blog-post_386.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")
# entry = soup.find(class_="entry")
# img = entry.find("img")
# src = img.get("src")
# print(src)


def getImageUrl(load_url):
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    entry = soup.find(class_="entry")
    img = entry.find("img")
    src = img.get("src")
    return src
print(getImageUrl(load_url))

# out_folder = Path("download_work")
# out_folder.mkdir(exist_ok=True)
# print("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVrKv05ATeRpW_i3mKfD0aQ-t78KFoBWEUhRCdTi-MiwwmJYUiIJ4NbVW4rg-bSj7GMwjDTm9EbTGeSS0XGo0uJCH9-0viaZFIvDDE6zVX5v3WcJR9kV5oOeYINO5QQnblEqknwS8DGBOU/s1600/pyoko_computer.png")