def solution(triangle):
    line = len(triangle)
    dp = [[] for _ in range(line)]
    for i in range(line):
        for j in range(i+1):
            # 위의 두개 합하기
            left, right = 0, 0
            if i > 0 and j > 0:
                left = dp[i-1][j-1]
            if i > 0 and j < i:
                right = dp[i-1][j]
            dp[i].append(triangle[i][j] + max(left, right))
    return max(dp[-1])