def solution(n,a,b):
    answer = 0
    mi = min(a, b)
    ma = max(a, b)
    for i in range(1, 21):
        if ma - mi == 1 and ma % 2 == 0:
            answer = i
            break
        ma = (ma + 1) // 2
        mi = (mi + 1) // 2
    return answer