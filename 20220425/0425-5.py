import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
bs = BeautifulSoup(response.text, "html.parser")
print(bs.select("a"))
