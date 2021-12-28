n = int(input())

arr = list(map(int, input().split()))

arr.sort()
cnt = 0
ans = 0

for i in arr:
    cnt += 1
    if cnt >= i:
        ans += 1
        cnt = 0

print(ans)
