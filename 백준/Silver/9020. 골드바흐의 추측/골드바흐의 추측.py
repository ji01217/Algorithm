import math

sieve = [False, False] + [True] * 10001
for i in range(int(math.sqrt(10000))+1):
    if sieve[i]:
        for j in range(2*i, 10001, i):
            sieve[j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    middle = n//2
    while sieve[middle] is False or sieve[n-middle] is False:
        middle -= 1
    print(middle, n-middle)