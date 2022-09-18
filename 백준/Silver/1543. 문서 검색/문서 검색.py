# 입력
Doc = input()
Word = input()

# 풀이
D = len(Doc)
W = len(Word)
ans = 0
for i in range(W):
    cnt = 0
    j = i
    while j < D - W + 1:
        for k in range(W + 1):
            if k == W:
                cnt += 1
                j += W
                break
            elif Doc[j + k] != Word[k]:
                j += 1
                break
    if ans < cnt:
        ans = cnt

# 출력
print(ans)