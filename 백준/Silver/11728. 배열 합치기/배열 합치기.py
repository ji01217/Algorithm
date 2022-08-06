# 입력
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 풀이
lst = [*A, *B]
lst.sort()

# 출력
print(*lst)