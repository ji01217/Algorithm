import sys


def func(lst):
    s_lst = sorted(lst, reverse=True)  # 내림차순 정렬
    ans = [0 for n in range(N)]
    dic = {}
    rank = 0
    temp = 3001  # 최대 정수 3000
    for s in s_lst:
        if temp > s:
            rank += 1
            dic[s] = rank
            temp = s
        else:  # temp = s
            rank += 1
    for l in lst:
        print(dic[l], end=' ')
    print()


N = int(sys.stdin.readline())
first = True
for i in sys.stdin:
    lst = list(map(int, i.split()))
    func(lst)
    if first:
        total = lst
        first = False
    else:
        for n in range(N):
            total[n] += lst[n]
func(total)