import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [[0] * (len(coins) + 1) for _ in range(k + 1)]

dp[0] = [1] * (len(coins) + 1)

for a in range(1, k + 1):
    for i in range(len(coins) - 1, -1, -1):
        dp[a][i] = dp[a][i + 1]
        if a - coins[i] >= 0:
            dp[a][i] += dp[a - coins[i]][i]

print(dp[k][0])
