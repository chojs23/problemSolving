n = int(input())
a = list(map(int, input().split()))

res = 0

l = r = 0
flag = 0
while r < n - 1:
    farthest = 0
    for i in range(l, r + 1):
        farthest = max(farthest, a[i] + i)
    l = r + 1
    r = farthest
    res += 1
    if r < l:
        flag = 1
        break
print(res if flag == 0 else -1)
