from collections import deque
from sys import stdin

input = stdin.readline

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
wc = [[False] * C for _ in range(R)]
sc = [[False] * C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()


def water():
    while wq1:
        x, y = wq1.popleft()
        a[x][y] = "."
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if a[nx][ny] == ".":
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wc[nx][ny] = True


def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if a[nx][ny] == ".":
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
    return False


for i in range(R):
    for j in range(C):
        if a[i][j] == "L":
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j
            a[i][j] = "."
        if a[i][j] == ".":
            wq1.append((i, j))
            wc[i][j] = True
while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)
