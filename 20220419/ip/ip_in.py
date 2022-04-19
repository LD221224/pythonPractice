import socket

in_addr = socket.gethostbyname(socket.gethostname())

in_addr2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr2.connect(("www.google.com", 443))
# 구글에 접속, https의 기본 접속 포트 443

print(in_addr)
print(in_addr2.getsockname()[0])
# 연결된 소켓의 이름 출력
