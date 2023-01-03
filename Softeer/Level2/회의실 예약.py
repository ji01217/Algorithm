N, M = map(int, input().split())
room = [input() for _ in range(N)]
room.sort()
arr = [[1] * 18 for _ in range(N)]
ans = [[] for _ in range(N)]
for _ in range(M):  # 회의시간 기록
    r, s, t = input().split()
    idx = room.index(r)
    for i in range(int(s), int(t)):
        arr[idx][i] = 0
for i in range(N):
    time = 9
    while time < 18:
        if arr[i][time] == 1:
            start = time
            for j in range(start, 18):
                if arr[i][j] == 0:
                    a = f"{str(time).zfill(2)}-{j}"
                    ans[i].append(a)
                    time = j
                    break
                if j == 17:
                    a = f"{str(time).zfill(2)}-18"
                    ans[i].append(a)
                    time = j
                    break
        time += 1

for i in range(N):
    print('Room ', room[i], ':', sep="")
    l = len(ans[i])
    if l == 0:
        print('Not available')
    else:
        print(f'{l} available:')
        for j in range(l):
            print(ans[i][j])
    if i == N-1:
        break
    print('-----')
