# 입력
W, H, X, Y, P = map(int, input().split())
players = [list(map(int, input().split())) for _ in range(P)]

# 풀이
ans = 0
for i in range(P):
    if X <= players[i][0] <= X + W:  # 만약 플레이어의 x좌표가 링크의 직사각형 안에 있다면
        if Y <= players[i][1] <= Y + H:  # 플레이어의 y좌표도 링크의 직사각형 안에 있을 때 +1
            ans += 1
    elif X - H/2 <= players[i][0] < X:  # 만약 플레이어의 x좌표가 링크의 왼쪽 반원에 해당된다면
        if ((players[i][0] - X) ** 2 + (players[i][1] - (Y + H/2)) ** 2) ** (1/2) <= H/2:
            ans += 1
    elif X + W < players[i][0] <= X + W + H/2:  # 만약 플레이어의 x좌표가 링크의 오른쪽 반원에 해당된다면
        if ((players[i][0] - (X + W)) ** 2 + (players[i][1] - (Y + H/2)) ** 2) ** (1/2) <= H/2:
            ans += 1

# 출력
print(ans)