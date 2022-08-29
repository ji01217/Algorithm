# 입력
ax, ay, bx, by, cx, cy = map(int, input().split())

# 풀이
# 세점이 일직선상으로 있다면 평행사변형을 만들 수 없다.
if (ax - bx) * (ay - cy) == (ay - by) * (ax - cx):
    print(-1.0)
else:
    ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    bc = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5
    ca = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5

    length = [ab + bc, bc + ca, ca + ab]
    ans = 2 * (max(length) - min(length))
    print(ans)