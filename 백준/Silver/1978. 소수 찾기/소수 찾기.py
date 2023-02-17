import math

N = int(input())
numbers = sorted(list(map(int, input().split())))
max_number = numbers[-1]
sieve = [False, False] + [True] * (max_number - 1)
for i in range(2, int(math.sqrt(max_number) + 1)):
    if sieve[i]:
        for j in range(2*i, max_number+1, i):
            sieve[j] = False
ans = 0
for number in numbers:
    if sieve[number]:
        ans += 1
print(ans)