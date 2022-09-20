# 입력
N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 풀이
ans = -1
for i in range(N):
    time = arr[i][0]
    cnt = 1
    while T > time and cnt < arr[i][2]:
        time += arr[i][1]
        cnt += 1
    if T <= time and cnt <= arr[i][2]:
        if ans == -1 or time - T < ans:
            ans = time - T

# 출력
print(ans)