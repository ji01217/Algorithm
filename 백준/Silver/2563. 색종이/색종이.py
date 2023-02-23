paper = [[0] * 101 for _ in range(101)]
ans = 0

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                ans += 1

print(ans)