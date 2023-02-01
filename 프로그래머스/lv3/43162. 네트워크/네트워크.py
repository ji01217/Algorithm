# DFS
def dfs(visited, i, computers, n):
    visited[i] = 1
    for j in range(n):
        if visited[j] == 0 and computers[i][j] == 1:
            dfs(visited, j, computers, n)
    return

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(visited, i, computers, n)
            answer += 1
    return answer