def solution(land):
    answer = 0
    n = len(land)
    dp = [[0 for _ in range(4)] for _ in range(n)]

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for j in range(4):
            tmp = dp[i - 1][j]
            dp[i - 1][j] = 0
            dp[i][j] = max(dp[i - 1]) + land[i][j]
            dp[i - 1][j] = tmp

    return max(dp[-1])
