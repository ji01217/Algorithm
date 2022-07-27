# 입력
while 1:
    try:
        N, M = map(int, input().split())
        # 풀이
        ans = 0
        for i in range(N, M + 1):
            com = set()
            str_i = str(i)
            for j in str_i:
                com.add(j)
            if len(com) == len(str_i):
                ans += 1

        # 출력
        print(ans)

    except:
        break