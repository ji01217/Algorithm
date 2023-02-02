def solution(answers):
    answer = []
    a, b, c = 0, 0, 0
    cnt = len(answers)
    aa = [1, 2, 3, 4, 5]
    ba = [2, 1, 2, 3, 2, 4, 2, 5]
    ca = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(cnt):
        if answers[i] == aa[i % 5]:
            a += 1
        if answers[i] == ba[i % 8]:
            b += 1
        if answers[i] == ca[i % 10]:
            c += 1
    score = max(a, b, c)
    if a == score:
        answer.append(1)
    if b == score:
        answer.append(2)
    if c == score:
        answer.append(3)
    return answer