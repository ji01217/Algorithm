from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    result = 1 # 연결된 node 수
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                result += 1
                queue.append(i)
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for start, not_visit in wires:
        visited = [0] * (n+1)
        visited[not_visit] = 1 # 방문하지 못하도록
        result = bfs(start, visited, graph)
        if answer > abs(n - 2 * result):
            answer = abs(n - 2 * result)
            
    return answer