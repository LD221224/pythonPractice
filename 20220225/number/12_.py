"""
조합 0의 개수

문제
(n
m)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n, m (0 ≤ m ≤ n ≤ 2,000,000,000)이 들어온다.

출력
첫째 줄에
(n
m)의 끝자리 0의 개수를 출력한다.
"""

"""
import math
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
answer = math.factorial(N)//math.factorial(K)//math.factorial(N-K)
s = str(answer)
for i in range(-1, -len(s)-1, -1):
    if s[i] != "0":
        print(abs(i + 1))
        break
"""
n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two


def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five


print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))
