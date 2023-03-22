from math import gcd

# 이미 심어져 있는 가로수 수
N = int(input())

# 가로수 간격을 저장할 배열
interval = []

# 첫번째 가로수 위치
tree = int(input())

# 간격 저장
for _ in range(1, N):
    next = int(input())
    interval.append(next-tree)
    tree = next

# 간격끼리의 최대공약수
result = gcd(*interval)

# 총 가로수 개수
ans = 0
for i in interval:
    ans += i // result - 1

print(ans)