# 입력
score = [(int(input()), i+1) for i in range(8)]

# 풀이
score.sort(reverse=True)
problem = []
ans = 0
for i in range(5):
    problem.append(score[i][1])
    ans += score[i][0]
problem.sort()

# 출력
print(ans)
print(*problem)