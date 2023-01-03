W, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
s_arr = sorted(arr, key=lambda x: -x[1])
ans = 0
weight = 0
for i in range(N):
    if weight == W:
        break
    if weight + s_arr[i][0] <= W:
        weight += s_arr[i][0]
        ans += s_arr[i][0] * s_arr[i][1]
    else:
        ans += (W - weight) * s_arr[i][1]
        break
print(ans)