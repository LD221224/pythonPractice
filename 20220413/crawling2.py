import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
html = requests.get(url)
bs_html = BeautifulSoup(html.content, 'html.parser')

location = bs_html.find_all('location')

for l in location:
    city = l.find('city').text
    print(city)
    w_list = re.findall(
        '<data>.+?'
        '<tmef>(.+?)</tmef>.+?'
        '<wf>(.+?)</wf>.+?'
        '<tmn>(.+?)</tmn>.+?'
        '<tmx>(.+?)</tmx>.+?'
        '<rnst>(.+?)</rnst>.+?'
        '</data>',
        str(l), re.DOTALL)
    for w in w_list:
        print(w[0], w[1], w[2], w[3], "강수확률:", w[4])

    print('-' * 30)
