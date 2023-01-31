def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if min(i + 1, citations[i]) > answer:
            answer = min(i + 1, citations[i])
    return answer