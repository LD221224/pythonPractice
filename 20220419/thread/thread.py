import threading
import time


def thread1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)


t1 = threading.Thread(target=thread1)
t1.daemon = True
# 데몬쓰레드로 설정하여 메인 동작이 실행될 때만 쓰레드 실행
t1.start()

while True:
    print("메인 동작")
    time.sleep(2.0)
