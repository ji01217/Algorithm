# 입력
N, M = map(int, input().split())
if N == 0 :
    print(0)
else:
    boxes = list(map(int, input().split()))

    # 풀이
    ans, now = 1, 0
    for i in range(N):
        if now + boxes[i] <= M:
            now += boxes[i]
        else:
            now = boxes[i]
            ans += 1


    # 출력
    print(ans)