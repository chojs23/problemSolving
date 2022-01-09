t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    for i in range(n):
        dp.append(list(arr[m * i : m * (i + 1)]))
    for c in range(1, m):
        for r in range(n):
            if r == 0:
                dp[r][c] = max(
                    dp[r][c - 1] + dp[r][c],
                    dp[r + 1][c - 1] + dp[r][c],
                )
            elif r == n - 1:
                dp[r][c] = max(
                    dp[r][c - 1] + dp[r][c],
                    dp[r - 1][c - 1] + dp[r][c],
                )
            else:
                dp[r][c] = max(
                    dp[r][c - 1] + dp[r][c],
                    dp[r + 1][c - 1] + dp[r][c],
                    dp[r - 1][c - 1] + dp[r][c],
                )
    maxgold = 0
    for r in range(n):
        maxgold = max(maxgold, dp[r][-1])
    print(maxgold)
