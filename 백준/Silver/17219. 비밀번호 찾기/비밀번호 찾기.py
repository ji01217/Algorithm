# 입력
N, M = map(int, input().split())
memo = {}
for _ in range(N):
    add, pw = input().split()
    memo[add] = pw
site = [input() for _ in range(M)]

# 풀이
for i in range(M):
    print(memo[site[i]])
