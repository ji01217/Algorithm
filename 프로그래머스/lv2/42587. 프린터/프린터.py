def solution(priorities, location):
    answer = 0
    priority = priorities[location]
    cnt = len(priorities)
    idx = 0
    while priorities[location] != 0:
        m = max(priorities)
        for i in range(cnt):
            now = (idx + i) % cnt
            if priorities[now] == m:
                priorities[now] = 0
                answer += 1
                idx = now
                break
    return answer