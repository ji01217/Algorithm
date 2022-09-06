# 입력
N = int(input())
lst = [int(input()) for _ in range(N)]

# 풀이
ans = 0
for i in range(N):
    cnt = 0
    for j in range(5):
        if lst[i] + j in lst:
            cnt += 1
    if ans < cnt:
        ans = cnt

# 출력
print(5 - ans)