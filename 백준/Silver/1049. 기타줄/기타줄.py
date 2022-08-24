# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# 풀이
group = one = 0xffffff
cnt = N // 6 + 1
for i in range(M):
    # 패키지
    if group > arr[i][0]:
        group = arr[i][0]
    # 낱개
    if one > arr[i][1]:
        one = arr[i][1]
# 패키지
a_ans = group * cnt
# 패키지 + 낱개
b_ans = group * (cnt - 1) + one * (N % 6)
# 낱개
c_ans = one * N

# 출력
print(min(a_ans, b_ans, c_ans))