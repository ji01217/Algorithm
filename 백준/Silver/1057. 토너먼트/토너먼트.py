# 입력
import math
N, A, B = map(int, input().split())

# 풀이
cnt = 0
while True:
    if abs(A-B) == 1 and min(A, B) % 2 == 1:
        print(cnt + 1)
        break
    if cnt == N:
        print(-1)
        break
    A = math.ceil(A/2)
    B = math.ceil(B/2)
    cnt += 1