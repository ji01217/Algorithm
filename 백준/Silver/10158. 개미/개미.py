# 입력
w, h = map(int,input().split())
p, q = map(int, input().split())
t = int(input())

# 풀이
# x축과 y축을 분리해서 생각하면
# w가 6일 때 x는 [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]의 형태로 움직이고
# h가 4일 때 y는 [0, 1, 2, 3, 4, 3, 2, 1]의 형태로 움직인다.

w_lst = []
h_lst = []

# w_lst
for i in range(w):
    w_lst.append(i)
for i in range(w, 0, -1):
    w_lst.append(i)

# h_lst
for i in range(h):
    h_lst.append(i)
for i in range(h, 0, -1):
    h_lst.append(i)

# t시간 후 개미의 좌표는 (초기 좌표 + t) % lst의 길이로 찾을 수 있다.
ans_x = w_lst[(p + t) % (2 * w)]
ans_y = h_lst[(q + t) % (2 * h)]

# 출력
print(ans_x, ans_y)