# 입력
arr = [list(map(int, input().split())) for _ in range(4)]

# 풀이
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = arr[i]
    # 겹치는 부분이 없을 경우
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    elif x1 == p2 or x2 == p1:
        # 겹치는 부분이 점일 경우
        if y1 == q2 or q1 == y2:
            print('c')
            continue
        # 겹치는 부분이 선분일 경우
        else:
            print('b')
            continue
    elif y1 == q2 or q1 == y2:
        print('b')
        continue
    # 그 외는 다 직사각형 모양으로 겹칠 경우
    else:
        print('a')