X = int(input())
total = 0
i = 1
while total+i < X:
    total += i
    i += 1
# 분모와 분자의 합이 i + 1
# i가 짝수면 왼쪽아래 방향 대각선, i가 홀수면 오른쪽 위 방향
if i % 2 == 1:
    de = X-total
    nu = i + 1 - de
    print(str(nu) + "/" + str(de))
else:
    nu = X - total
    de = i + 1 - nu
    print(str(nu) + "/" + str(de))
