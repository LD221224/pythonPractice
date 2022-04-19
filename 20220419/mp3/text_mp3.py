# pip install gtts : 문자를 음성으로 변환해주는 라이브러리
# pip install playsound : mp3파일을 파이썬에서 재생하기위한 라이브러리

from gtts import gTTS
from playsound import playsound

# text = "안녕하세요. 파이썬과 40개의 작품들 입니다."
# tts = gTTS(text=text, lang='ko')
# tts.save(r"mp3\hi.mp3")
# playsound(r"mp3\hi.mp3")

file_path = r'mp3/text.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"mp3/text.mp3")

playsound(r"mp3/text.mp3")
