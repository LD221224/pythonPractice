from urllib import response
import urllib.request

request = urllib.request.Request('https://www.naver.com')

response = urllib.request.urlopen(request)

htmlBytes = response.read()
htmlStr = htmlBytes.decode('utf-8')

htmlSplit = htmlStr.split('\n')

for line in htmlSplit:
    print(line)
