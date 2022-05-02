from bs4 import BeautifulSoup
import requests
import pandas

url = "https://www.melon.com/chart/index.htm"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 " \
             "Safari/537.36 Edg/92.0.902.67 "
header = {'User-Agent': user_agent}

response = requests.get(url, headers=header)
print(response)

soup = BeautifulSoup(response.text, "html.parser")
song_list = soup.find_all('div', 'ellipsis rank01')
artist_list = soup.find_all('span', 'checkEllipsis')

song = []
for i in song_list:
    song.append(i.text.replace('\n', ''))

artist = []
for i in artist_list:
    artist.append(i.text)

# for i in range(0, 100):
#     print(f"{i + 1}위 : {song[i]} - {artist[i]}")


# pandas 사용
ranking = []
for i in range(1, 101):
    ranking.append(i)

music = pandas.DataFrame()
music['제목'] = song
music['가수'] = artist
music['랭킹'] = ranking
music.set_index('랭킹', inplace=True)
print(music)

file_csv = r"C:\pythonPractice\20220425\0425-6.csv"
music.to_csv(file_csv, encoding='utf-8-sig')
