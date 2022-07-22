# 입력
C, R = map(int, input().split())
K = int(input())

# 풀이
visited = [[0] * (R + 1) for _ in range(C + 1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 1
dir = 0
cx, cy = 1, 1
visited[cy][cx] = 1

if K > C * R:
    print(0)
else:
    while cnt < K:
        while 0 < cx + dx[dir] <= R and 0 < cy + dy[dir] <= C and visited[cy + dy[dir]][cx + dx[dir]] == 0 and cnt < K:
            cx = cx + dx[dir]
            cy = cy + dy[dir]
            visited[cy][cx] = 1
            cnt += 1
        if dir == 3:
            dir = 0
        else:
            dir += 1
    print(cy, cx)