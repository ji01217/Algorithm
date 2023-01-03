M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
user = list(map(int, input().split()))
ans = 'normal'
for n in range(N-M+1):
    if user[n] == secret[0]:
        for m in range(M):
            if user[n+m] != secret[m]:
                break
            if m == M - 1:
                ans = 'secret'
print(ans)