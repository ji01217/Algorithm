# 입력
N, K = map(int, input().split())
tem = list(map(int, input().split()))

# 풀이
cur = 0
for i in range(K):
    cur += tem[i]
ans = cur
for i in range(1, N - K + 1):
    cur = cur - tem[i - 1] + tem[i + K - 1]
    if ans < cur:
        ans = cur

# 출력
print(ans)