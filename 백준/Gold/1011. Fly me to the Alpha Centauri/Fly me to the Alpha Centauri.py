T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dis = y - x
    k = 1
    cnt = 0

    while dis > 0:
        dis = dis - k
        cnt += 1
        if dis <= 0:
            break
        else:
            dis = dis - k
            cnt += 1
        k += 1

    print(cnt)