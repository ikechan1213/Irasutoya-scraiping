import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url = "https://www.irasutoya.com/2021/01/onepiece.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

out_folder = Path("download2")
out_folder.mkdir(exist_ok=True)

entry = soup.find(class_="entry")
for element in entry.find_all("img"):
    src = element.get("src")

    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)

    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    #画像の保存
    with open(out_path, "wb") as f:
        f.write(imgdata.content)

        #1秒待機
        time.sleep(1)