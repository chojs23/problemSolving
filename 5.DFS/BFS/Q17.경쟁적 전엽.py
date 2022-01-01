from sys import stdin
from collections import deque


n, k = map(int, input().split())

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


data = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            data.append((board[i][j], 0, i, j))

data.sort()
queue = deque(data)


def bfs(queue, s):
    while queue:
        virus, time, x, y = queue.popleft()
        if time == s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == 0:

                    board[nx][ny] = virus
                    queue.append((virus, time + 1, nx, ny))


bfs(queue, s)

print(board[x - 1][y - 1])
