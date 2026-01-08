import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

resultUrl = "https://www.irasutoya.com/search?q=%E9%87%8E%E7%90%83&updated-max=2019-06-24T15:00:00%2B09:00&max-results=20&start=0&by-date=false"

urls = []

html = requests.get(resultUrl)
soup = BeautifulSoup(html.content, "html.parser")
urls = list(set(urls))

for link in soup.find_all("a"):
    href = link.get("href")
    if href is None:
        continue
    if "irasutoya.com/" in href and "blog-post" in href and "#" not in href:
        urls.append(href)



for u in urls:
    print(u)