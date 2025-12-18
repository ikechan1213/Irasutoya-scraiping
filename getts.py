import requests

url = "https://www.irasutoya.com/"
response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)
