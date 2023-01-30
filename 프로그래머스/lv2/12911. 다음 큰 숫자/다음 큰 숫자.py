def solution(n):
    answer = 0
    a = n
    n1 = bin(n).count("1")
    while True:
        a += 1
        n2 = bin(a).count("1")
        if n1 == n2:
            answer = a
            break
    return answer