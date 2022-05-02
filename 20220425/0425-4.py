import requests
response = requests.get("https://www.naver.com")

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)
