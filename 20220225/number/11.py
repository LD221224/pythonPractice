"""
팩토리얼 0의 개수

문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""
import math
import sys

N = int(sys.stdin.readline())
N_fac = str(math.factorial(N))
for i in range(-1, -len(N_fac)-1, -1):
    if N_fac[i] != "0":
        print(abs(i + 1))
        break
