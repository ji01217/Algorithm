import math
# 입력
N, M, K = map(int, input().split())


# 풀이
def combination(n, r):
    if n < r:
        return 0
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))


def possibility(n, m, k):
    return combination(m, k) * combination(n-m, m-k) / combination(n,m)


ans = 0
for i in range(K, M + 1):
    ans += possibility(N, M, i)

# 출력
print(ans)