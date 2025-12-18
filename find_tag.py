import requests
from bs4 import BeautifulSoup

load_url = "https://www.irasutoya.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup.find_all("title"))
print(soup.find_all("h2"))
print(soup.find_all("li"))
