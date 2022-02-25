"""
이항 계수 1

문제
자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

출력
(N
K)를 출력한다.
"""
import math
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
answer = math.factorial(N)//math.factorial(K)//math.factorial(N-K)
print(answer)
