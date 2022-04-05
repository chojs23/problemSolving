import sys

input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c, d):
    global ans
    if a[r][c] == 0:
        a[r][c] = 2
        ans += 1

    for i in range(4):
        nd = (d + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if a[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]

    if a[nr][nc] == 1:
        return
    clean(nr, nc, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)
