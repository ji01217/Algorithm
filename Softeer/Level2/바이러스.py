K, P, N = map(int, input().split())
ans = K
for n in range(N):
    ans = ans * P % 1000000007
print(ans)