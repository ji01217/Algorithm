import math

M, N = map(int, input().split())

sieve = [False, False] + [True] * (N-1)

for i in range(2, int(math.sqrt(N)+1)):
    if sieve[i] == True:
        for j in range(2*i, N+1, i):
            sieve[j] = False

for i in range(M, N+1):
    if sieve[i]:
        print(i)