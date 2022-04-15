import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(str, input().rstrip())))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

visited = [[0 for _ in range(N)] for _ in range(N)]


def dfs(x, y, color):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (
            0 <= nx < N
            and 0 <= ny < N
            and graph[nx][ny] == color
            and visited[nx][ny] == 0
        ):
            dfs(nx, ny, color)
    return True


res1 = 0
res2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and dfs(i, j, graph[i][j]):
            res1 += 1
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and dfs(i, j, graph[i][j]):
            res2 += 1


print(res1, res2)
