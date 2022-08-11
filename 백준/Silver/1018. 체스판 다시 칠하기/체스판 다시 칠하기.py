# 입력
N, M = map(int, input().split())
arr = []
ans = []
for _ in range(N):
    arr.append(input())

# 풀이
# 시작점 si, sj
for si in range(N - 7):
    for sj in range(M - 7):
        W_cnt = 0  # 첫번째 칸이 W
        for i in range(si, si + 8):
            for j in range(sj, sj + 8):
                if (i + j) % 2 == 0:
                    if arr[i][j] != 'W':
                        W_cnt += 1
                else:
                    if arr[i][j] != 'B':
                        W_cnt += 1
        ans.append(min(W_cnt, 64-W_cnt))

# 출력
print(min(ans))