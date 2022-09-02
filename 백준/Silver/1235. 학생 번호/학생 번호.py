# 입력
N = int(input())
lst = [input() for _ in range(N)]

# 풀이
length = len(lst[0])
for i in range(1, length + 1):
    number = set()
    for j in range(N):
        number.add(lst[j][-i:])
    if len(number) == N:
        print(i)
        break