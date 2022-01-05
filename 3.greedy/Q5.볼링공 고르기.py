n, m = map(int, input().split())

w = list(map(int, input().split()))
ans = 0

ball = [0] * 10
for i in w:
    ball[i] += 1

for i in ball:
    n -= i
    ans += i * n

print(ans)
