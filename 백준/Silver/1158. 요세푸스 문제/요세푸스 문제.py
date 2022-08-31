# 입력
N, K = map(int, input().split())

# 풀이
lst = [i for i in range(1, N + 1)]
ans = []
num = 0
for i in range(N):
    num += K - 1
    if num >= len(lst):
        num %= len(lst)
    ans.append(lst.pop(num))

# 출력
ans_str = str(ans)[1:-1]
print('<', ans_str, '>', sep='')