def minus(i, n):
    global answer, cnt, tg, nb
    if i == cnt-1:
        if n-nb[i] == tg:
            answer += 1
        return
    minus(i+1, n-nb[i])
    plus(i+1, n-nb[i])
    return

def plus(i, n):
    global answer, cnt, tg, nb
    if i == cnt-1:
        if n+nb[i] == tg:
            answer += 1
        return
    minus(i+1, n+nb[i])
    plus(i+1, n+nb[i])
    return

def solution(numbers, target):
    global answer, cnt, tg, nb
    nb = numbers
    tg = target
    answer = 0
    cnt = len(numbers)
    minus(0, 0)
    plus(0, 0)
    return answer