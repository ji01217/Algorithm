from collections import deque
import sys
H, K, R = map(int, sys.stdin.readline().split())
q_tail = deque()
for _ in range(2**H):
    q_tail.append(list(map(int, sys.stdin.readline().split())))
queue = deque([[], []] for _ in range(2**H))
for r in range(1, R+1):
    check = (r+1) % 2  # 홀수일 때 check=1, 짝수일 때 check=0
    for i in range(1, 2**H):
        if queue[i][check]:
            queue[i//2][i%2].append(queue[i][check].pop(0))
        elif queue[i][r%2]:
            queue[i//2][i%2].append(queue[i][r%2].pop(0))
    for i in range(2**H):
        a = 2**H + i
        queue[a // 2][a % 2].append(q_tail[i].pop(0))
ans = 0
for q in queue[0][1]:
    ans += q
print(ans)