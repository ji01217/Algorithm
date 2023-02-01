def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        s, r = divmod(i, n)
        answer.append(max(s+1, r+1))
    return answer