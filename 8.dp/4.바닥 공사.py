N = int(input())

dp = [0]*1001

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4, N+1):
    dp[i] = dp[i-2]+dp[i-1]*2

print(dp)
