n, m = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))

dp = [10001]*(m+1)

dp[0] = 0
for i in range(n):
    for j in range(num[i], m+1):
        if dp[j-num[i]] != 10001:
            dp[j] = min(dp[j], dp[j-num[i]]+1)

if dp[m] == 10001:
    print("-1")
else:
    print(dp[m])
