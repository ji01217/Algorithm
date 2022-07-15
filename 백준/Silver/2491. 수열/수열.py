# 입력
N = int(input())
lst = list(map(int, input().split()))

# 풀이
cnt = 1
ans = 1
for i in range(1, N):
    if lst[i] <= lst[i - 1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt
cnt = 1
for i in range(1, N):
    if lst[i] >= lst[i - 1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

# 출력
print(ans)