# 그리디
N = int(input())
ans = 0
while N > 0 and N % 5 != 0:
    ans += 1
    N -= 3
if N % 5 == 0:
    ans += N // 5
else:
    ans = -1
print(ans)