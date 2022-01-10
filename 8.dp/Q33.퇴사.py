n = int(input())

t = []
p = []
dp = [0] * (n + 1)
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

max_value = 0

for i in range(n - 1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(p[i] + dp[t[i] + i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max(dp))
