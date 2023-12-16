# DP
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    # 1 1 2 3 5
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
    return dp[n]
