def solution(n, s):
    answer = [-1]
    if s < n:
        return answer
    s, r = divmod(s, n)
    answer = [s] * n
    for i in range(r):
        answer[i] += 1
    answer.sort()
    return answer