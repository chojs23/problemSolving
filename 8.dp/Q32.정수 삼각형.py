import copy

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = copy.deepcopy(arr)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif j == i:
            dp[i][j] = dp[i][j] + dp[i - 1][-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[-1]))
