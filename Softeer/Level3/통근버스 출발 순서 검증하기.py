import sys

N = int(sys.stdin.readline())
bus = list(map(int, sys.stdin.readline().split()))
ans = 0
arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N - 2):
    ai = bus[i]
    arr[ai][N] = 0
    for n in range(N - 1, 0, -1):
        if bus[n] < ai:
            arr[ai][n] = arr[ai][n + 1] + 1
        else:
            arr[ai][n] = arr[ai][n + 1] + 0
    for j in range(i + 1, N-1):
        aj = bus[j]
        if ai < aj:
            ans += arr[ai][j]

print(ans)