N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(M)]
limit = [[0, 0]]
test = [[0, 0]]
for n in range(N):
    limit.append([limit[n][0]+a[n][0], a[n][1]])
for m in range(M):
    test.append([test[m][0]+b[m][0], b[m][1]])
ans = 0
for n in range(1, N+1):
    l_min = limit[n-1][0]
    l_max = limit[n][0]
    for m in range(1, M+1):
        t_min = test[m-1][0]
        t_max = test[m][0]
        if l_min >= t_max or l_max <= t_min: # 겹치지 않는다면
            continue
        else:
            if ans < test[m][1] - limit[n][1]:
                ans = test[m][1] - limit[n][1]
print(ans)