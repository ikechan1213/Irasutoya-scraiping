import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def readResultHtml(targetUrl, urls):

    current_url = targetUrl

    while current_url:
        resp = requests.get(current_url)
        soup = BeautifulSoup(resp.content, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if not href:
                continue
            if "irasutoya.com/" in href and "blog-post" in href and "#" not in href:
                urls.add(href)

        next_link = soup.find("a", class_="blog-pager-older-link")
        if next_link:
            current_url = urljoin(current_url, next_link.get("href"))
        else:
            break

    return list(urls)

if __name__ == "__main__":
    resultUrl = "https://www.irasutoya.com/search?q=%E9%87%8E%E7%90%83&updated-max=2019-06-24T15:00:00%2B09:00&max-results=20&start=0&by-date=false"
    urls = set()
    urls_list = readResultHtml(resultUrl, urls)
    for u in urls_list:
        print(u)