# 입력
N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]

# 풀이
P.sort(reverse=True)
ans_price = ans_revenue = 0
for i in range(min(N, M)):
    if P[i] * (i + 1) > ans_revenue:
        ans_revenue = P[i] * (i + 1)
        ans_price = P[i]

# 출력
print(ans_price, ans_revenue)