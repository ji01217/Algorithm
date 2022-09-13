# 입력
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 풀이
A.sort()
B.sort(reverse=True)
ans = 0
for i in range(N):
    ans += A[i] * B[i]

# 출력
print(ans)