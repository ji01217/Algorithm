def solution(n):
    p = [0] * (2001)
    p[1] = 1
    p[2] = 2
    for i in range(3, n+1):
        p[i] = p[i-2] + p[i-1]
    return p[n] % 1234567
