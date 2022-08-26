# 입력
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 풀이
check = min(N, M)
ans = 1
for i in range(N):
    for j in range(M):
        for k in range(check, 0, -1):
            if i + k < N and j + k < M and arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]:
                ans = max(ans, (k + 1)**2)
                break

# 출력
print(ans)