def possible(item1, item2, symbol):
    if symbol == "<":
        return item1 < item2
    if symbol == ">":
        return item1 > item2


def backtracking(idx, string):
    global min_value
    global visited
    global max_value
    if idx == n + 1:
        if not len(min_value):
            min_value = string
        else:
            max_value = string
        return
    for i in range(10):
        if visited[i]:
            continue
        if idx == 0 or possible(string[-1], str(i), stack[idx - 1]):
            visited[i] = True
            backtracking(idx + 1, string + str(i))
            visited[i] = False


0
n = int(input())
stack = list(input().split())
max_value = ""
min_value = ""
visited = [False] * 10
backtracking(0, "")
print(max_value)
print(min_value)
