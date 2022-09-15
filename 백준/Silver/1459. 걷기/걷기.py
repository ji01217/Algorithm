# 입력
X, Y, W, S = map(int, input().split())

# 풀이
# 1. 가로, 세로로만 이동
dis1 = (X + Y) * W
# 2. 대각선으로만 이동 (지그재그로)
# 2-1. X + Y가 홀수일 때 마지막 한 번만 가로 or 세로
if (X + Y) % 2:
    dis2 = (max(X, Y) - 1) * S + W
# 2-2. X + Y가 짝수일 때
else:
    dis2 = max(X, Y) * S
# 3. 대각선 + 가로 or 세로
dis3 = min(X, Y) * S + abs(X - Y) * W

# 출력
print(min(dis1, dis2, dis3))