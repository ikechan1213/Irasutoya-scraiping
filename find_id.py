import requests
from bs4 import BeautifulSoup

load_url = "https://www.irasutoya.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

lbl1 = soup.find(id="Label1")
for element in lbl1.find_all("li"):
    print(element.text)