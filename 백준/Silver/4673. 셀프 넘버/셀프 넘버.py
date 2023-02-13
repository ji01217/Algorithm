lst = [0 for _ in range(10001)]

for i in range(10000):
    num = i
    for j in str(i):
        num += int(j)
    if num <= 10000:
        lst[num] = 1

for i in range(1, 10001):
    if lst[i] == 0:
        print(i)