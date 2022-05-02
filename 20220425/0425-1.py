from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

html_class = soup.find_all(class_='news_tit')

# print(html_class)

for t in html_class:
    title = t.text.strip()
    print(title)
