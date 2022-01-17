import sys

input = sys.stdin.readline
n, s, m = map(int, input().split())

v = list(map(int, input().split()))

dp = []
for _ in range(n + 1):
    dp_arr = [False] * (m + 1)
    dp.append(dp_arr)
dp[0][s] = True

for i in range(n):
    for j in range(m + 1):
        check = dp[i][j]
        if check:
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = True
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = True
result = -1
for i in range(m + 1):
    if dp[n][i]:
        result = i

print(result)
