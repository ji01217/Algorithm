# 입력
L = int(input())
S = list(map(int, input().split()))
n = int(input())

# 풀이
S.sort()
if n in S:
    print(0)
else:
    less = greater = 0
    for i in S:
        if i < n:
            less = i
        elif i > n and greater == 0:
            greater = i
    less += 1
    greater -= 1
    print((n - less) * (greater - n + 1) + (greater - n))