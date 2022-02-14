"""
쉬운 계단 수

문제
45656이란 수를 보자.
이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자.
0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""
N = int(input())
a = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    a[1][i] = 1

for i in range(1, N):
    # 끝이 0과 9인 경우 0 -> 1, 9 -> 8
    a[i + 1][0] = a[i][1]
    a[i + 1][9] = a[i][8]
    for j in range(1, 9):
        a[i + 1][j] = a[i][(j + 1) % 10] + a[i][(j + 9) % 10]

print(a)
print(sum(a[-1]) % (10**9))