def solution(s):
    a1, a2 = 0, 0
    while s != "1":
        a1 += 1
        ns = 0
        for i in s:
            if i == "0":
                a2 += 1
            if i == "1":
                ns += 1
        s = str(bin(ns))[2:]
    answer = [a1, a2]
    return answer