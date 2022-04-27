import sys


input = sys.stdin.readline


N, M = map(int, input().rstrip().rsplit())

memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

max_cost = sum(cost) + 1
dp = [[0] * max_cost for _ in range(N + 1)]

MIN = max_cost

for i in range(1, N + 1):
    for j in range(len(dp[0])):
        if j < cost[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

        if dp[i][j] >= M and MIN > j:
            MIN = j

print(MIN)
