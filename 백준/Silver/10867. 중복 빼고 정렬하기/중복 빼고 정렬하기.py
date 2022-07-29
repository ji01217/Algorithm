# 입력
N = int(input())
numbers=set(map(int, input().split()))
lst = list(numbers)

# 풀이
lst.sort()

# 출력
print(*lst)