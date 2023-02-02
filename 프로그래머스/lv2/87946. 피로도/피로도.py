def dfs(dungeons, visited, cnt, i, fatigue):
    global answer, total
    visited[i] = 1
    fatigue -= dungeons[i][1]
    cnt += 1
    if answer < cnt:
        answer = cnt
    for j in range(total):
        if visited[j] == 0 and fatigue >= dungeons[j][0]:
            dfs(dungeons, visited, cnt, j, fatigue)
    visited[i] = 0
    return

def solution(k, dungeons):
    global answer, total
    answer = 0
    total = len(dungeons)
    cnt = 0
    for i in range(total):
        visited = [0] * total
        if k >= dungeons[i][0]:
            dfs(dungeons, visited, 0, i, k)
    return answer