"""
스도쿠

문제
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.
나머지 빈 칸을 채우는 방식은 다음과 같다.
각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다.
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

"""
import sys

sdoku = []
for _ in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().rstrip().split())))

line = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 가로줄
for i in range(9):
    if 0 in sdoku[i]:
        count = sdoku[i].count(0)
        if count == 1:
            index_0 = sdoku[i].index(0)
            sdoku[i][index_0] = sum(line) - sum(sdoku[i])

print(sdoku)

# 세로줄
for i in range(9):
    temp = []
    for j in range(9):
        temp.append(sdoku[j][i])
    if 0 in temp:
        count = temp.count(0)
        if count == 1:
            index_0 = temp.index(0)
            sdoku[index_0][i] = sum(line) - sum(temp)
print(sdoku)
