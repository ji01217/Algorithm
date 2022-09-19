# 입력
N = int(input())
lst = [input() for _ in range(N)]

# 풀이
ans = [lst[0]*2]
for i in range(1, N):
    for j in range(len(ans)):
        if lst[i] in ans[j] and len(lst[i]*2) == len(ans[j]):
            break
        if j == len(ans) - 1:
            ans.append(lst[i]*2)

# 출력
print(len(ans))