n = int(input())

data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_num = 1e9
max_num = -1e9


def dfs(i, now):
    global add, sub, mul, div, max_num, min_num
    if i == n:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1


dfs(1, data[0])
print(max_num)
print(min_num)
