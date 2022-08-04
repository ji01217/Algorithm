# 입력
import sys
input = sys.stdin.readline
N = int(input()) - 7
score = [float(input()) for _ in range(7)]

# 풀이
score.sort()
i = 0
while i < N:
    score.append(float(input()))
    score.sort()
    score.pop()
    i += 1

# 출력
for i in range(7):
    print("{:.3f}".format(score[i]))