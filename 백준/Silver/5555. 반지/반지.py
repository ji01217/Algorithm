# 입력
text = input()
N = int(input())
arr = [input() for _ in range(N)]

# 풀이
ans = 0
for i in range(N):
    arr[i] = arr[i] * 2
    if text in arr[i]:
        ans += 1

# 출력
print(ans)