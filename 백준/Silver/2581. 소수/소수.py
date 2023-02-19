import math

M = int(input())
N = int(input())

sieve = [False, False] + [True] * (N - 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if sieve[i]:
        for j in range(i * 2, N + 1, i):
            sieve[j] = False

ans = []
for i in range(M, N + 1):
    if sieve[i]:
        ans.append(i)
if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
