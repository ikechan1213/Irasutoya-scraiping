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

#画像保存先フォルダの作成
out_folder = Path("download_work")
out_folder.mkdir(exist_ok=True)
#画像の取得処理
imgdata = requests.get(getImageUrl(load_url))
filename = getImageUrl(load_url).split("/")[-1]
out_path = out_folder.joinpath(filename)

#画像DLフォルダを書き込みモードで開く
f = open(out_path, "wb")
#画像データの書き込み
f.write(imgdata.content)
#ファイルを閉じて保存している
f.close()