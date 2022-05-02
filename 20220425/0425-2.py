from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82" \
      "%A0%EC%94%A8 "
html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

temperature = soup.find(class_='temperature_text')
print(temperature.text)

weather = soup.find(class_='weather before_slash')
print(weather.text)
