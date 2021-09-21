import sys

N = int(sys.stdin.readline().rstrip())
food = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0]*N
dp[0] = food[0]
dp[1] = max(food[1], food[0])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+food[i])

print(max(dp))
