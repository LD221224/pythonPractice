"""
좌표 압축

문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109
"""
import sys

N = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))
y = sorted(list(set(x)))
dic = dict()
for i in range(len(y)):
    dic[y[i]] = i
for i in range(N):
    print(dic[x[i]], end=" ")
"""
x = sys.stdin.readline().rstrip().split()
y = list(set(x))
for i in range(N):
    count = 0
    for j in range(len(y)):
        if x[i] > y[j]:
            count += 1
    print(count, end=" ")
"""
