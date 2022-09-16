# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 풀이
arr.sort(key=lambda x: x[0])
ans = 0
price = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] <= arr[j][0]:
            if arr[i][0] >= arr[j][1]:
                cnt = cnt + arr[i][0] - arr[j][1]
    if ans < cnt:
        ans = cnt
        price = arr[i][0]

# 출력
print(price)