# 입력
N, score, P = map(int, input().split())
if N:
    lst = list(map(int, input().split()))

    # 풀이
    if N == P and lst[-1] >= score:
        print(-1)
    else:
        ans = N + 1
        for i in range(N):
            if lst[i] <= score:
                ans = i + 1
                break
        print(ans)
else:
    print(1)