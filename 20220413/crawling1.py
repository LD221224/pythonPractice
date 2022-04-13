import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
html = requests.get(url)

print(html)
# print(html.text)

bs_html = BeautifulSoup(html.content, "html.parser")

logo_naver = bs_html.find("a", {"class": "logo_naver"})

print(logo_naver)
print(logo_naver.text)

url_daum = "https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png"
req = requests.get(url_daum)
file = open("daum_logo.png", "wb")
file.write(req.content)
file.close()
