s = list(map(int, input()))

ans = 0
for num in s:
    if num == 0 or num == 1 or ans == 0:
        ans += num
    else:
        ans *= num
print(ans)
