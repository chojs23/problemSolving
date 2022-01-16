n = int(input())
a = list(map(int, input().split()))

dp = [999999] * (n + 100)

dp[0] = 0

for i in range(n):

    for j in range(a[i]):
        dp[i + j + 1] = min(dp[i] + 1, dp[i + j + 1])

print(dp[n - 1] if dp[n - 1] != 999999 else -1)
