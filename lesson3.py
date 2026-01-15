# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# from pathlib import Path
#
# def readResultHtml(targetUrl, urls):
#
#     current_url = targetUrl
#
#     while current_url:
#         resp = requests.get(current_url)
#         soup = BeautifulSoup(resp.content, "html.parser")
#
#         for link in soup.find_all("a"):
#             href = link.get("href")
#             if not href:
#                 continue
#             if "irasutoya.com/" in href and "blog-post" in href and "#" not in href:
#                 urls.add(href)
#
#         next_link = soup.find("a", class_="blog-pager-older-link")
#         if next_link:
#             current_url = urljoin(current_url, next_link.get("href"))
#
#
#         else:
#             break
#     def downloadImage(img_URL):
#         out_folder = Path("download_baseball")
#         out_folder.mkdir(exist_ok=True)
#         imgdata = requests.get(current_url)
#         filename = current_url.split("/")[-1]
#         out_path = out_folder.joinpath(filename)
#         f = open(out_path, "wb")
#         f.write(imgdata.content)
#         f.close()
#
#     return list(urls)
#
#
#
#
#
# if __name__ == "__main__":
#     resultUrl = "https://www.irasutoya.com/search?q=%E9%87%8E%E7%90%83&updated-max=2019-06-24T15:00:00%2B09:00&max-results=20&start=0&by-date=false"
#     urls = set()
#     urls_list = readResultHtml(resultUrl, urls)
#     for u in urls_list:
#         print(u)
import requests
from bs4 import BeautifulSoup
import os

inputword = "野球"
URLs = set()
def getSearchUrls(inputword):
    next_url = "https://www.irasutoya.com/search?q=" + inputword

    while next_url:
        html = requests.get(next_url)
        soup = BeautifulSoup(html.content, "html.parser")

        # 検索結果一覧の本体
        main = soup.find("div", class_="blog-posts")

        # 記事URL取得
        for a in main.find_all("a"):
            href = a.get("href")
            if href and "blog-post" in href:
                href = href.split("#")[0]
                URLs.add(href)

        # 次のページ
        next_link = soup.find("a", class_="blog-pager-older-link")
        if next_link:
            next_url = next_link.get("href")
        else:
            break
    return URLs
urls = getSearchUrls(inputword)
def getImages(urls):
    image_urls = set()
    for url in urls:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        blocks = soup.find_all("div", class_="separator")

        for block in blocks:
            imgs = block.find_all("img")
            for img in imgs:
                src = img.get("src")
                if src:
                    image_urls.add(src)
    return image_urls



def downloadImages(image_urls):
    os.makedirs("images", exist_ok=True)

    i = 1
    for img_url in image_urls:
        print("DL-URL:", img_url)

        r = requests.get(img_url)
        if r.status_code == 200:
            with open(f"images/img_{i}.jpg", "wb") as f:
                f.write(r.content)
            i += 1

urls = getSearchUrls(inputword)
images = getImages(urls)
downloadImages(images)
print("全ダウンロード完了")