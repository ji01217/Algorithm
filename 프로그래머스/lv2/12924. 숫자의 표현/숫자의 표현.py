def solution(n):
    answer = 0
    for i in range(1, n+1):
        ssum = i
        a = 1
        while ssum <= n:
            if ssum == n:
                answer += 1
            ssum += i + a
            a += 1
    return answer