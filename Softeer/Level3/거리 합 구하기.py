import sys
sys.setrecursionlimit(10**6)


def dfs1(current, parent):
    subtreeSize[current] = 1
    for l in range(len(node[current])):
        child = node[current][l][0]
        weight = node[current][l][1]
        if child != parent:
            dfs1(child, current)
            subtreeSize[current] += subtreeSize[child]
            distSum[current] += distSum[child] + subtreeSize[child] * weight
    return


def dfs2(current, parent):
    for l in range(len(node[current])):
        child = node[current][l][0]
        weight = node[current][l][1]
        if child != parent:
            distSum[child] = distSum[current] + weight * (N - 2*subtreeSize[child])
            dfs2(child, current)
    return


N = int(sys.stdin.readline())
node = [[] for _ in range(N+1)]
subtreeSize = [0 for _ in range(N+1)]
distSum = [0 for _ in range(N+1)]
for s in sys.stdin:
    x, y, t = map(int, s.split())
    node[x].append([y, t])
    node[y].append([x, t])
dfs1(1, 1)
dfs2(1, 1)
for n in range(1, N + 1):
    print(distSum[n])