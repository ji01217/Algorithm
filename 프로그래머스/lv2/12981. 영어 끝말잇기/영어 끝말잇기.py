def solution(n, words):
    a1, a2 = 0, 0
    length = len(words)
    s = {words[0]}
    for i in range(1, length):
        if words[i-1][-1] != words[i][0]:
            a1 = (i + 1) % n
            a2 = (i + 1) // n + 1
            if a1 == 0:
                a1 = n
                a2 -= 1
            break
        s.add(words[i])
        if len(s) != i + 1:
            a1 = (i + 1) % n
            a2 = (i + 1) // n + 1
            if a1 == 0:
                a1 = n
                a2 -= 1
            break
    return [a1, a2]