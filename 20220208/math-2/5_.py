"""
베르트랑 공준

문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는
적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
"""

def decimal(n):
    a = []
    for i in range(n + 1, (2 * n) + 1):
        chk = 0
        if i != 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    chk = 1
                    break
            if chk == 0:
                a.append(i)
    print(len(a))


while True:
    n = int(input())
    if n == 0:
        break
    decimal(n)

"""
max_num = 123456*2+1                         # 문제에서 제시한 최대값 끝
check_list = [True for i in range(max_num)]  # 우선 전부 True 값으로 만든다

for i in range(2, int(max_num**0.5)+1):      # 에라토스테네스의 체 알고리즘
	if check_list[i] == True:                # True면 소수
		j = 2                                # False면 소수가 아니다
		while i * j <= max_num:              # check_list의 인덱스가 실제 값이다.
			check_list[i*j] = False
			j += 1
			
while True:                          # 0을 입력받을 때까지 돌기 위한 반복문
	cnt = 0                          # 개수를 셀 cnt 변수 선언
	a = int(input())                 # 범위의 최소값 입력받기
	b = 2 * a                        # 범위의 끝 값 b에 담기
	if a == 0:                       # 만약 0을 입력 받았으면 탈출
		break
		
	for i in range(a+1,b+1):         # 검사할 수의 범위를 검사하기 위한 반복문
		if check_list[i]:            # 범위의 수를 하나씩 check_list에 인덱스에 넣어본다
			cnt += 1                 # 만약 소수면 카운트 업
	print(cnt)                       # 다 돌았음 개수 출력
"""