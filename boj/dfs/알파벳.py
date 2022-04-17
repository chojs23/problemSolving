import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input().rstrip()))
cnt = 0

dc, dr = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = set()


def dfs(r, c):
    global cnt
    visit.add(board[r][c])
    cnt = max(cnt, len(visit))
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (
            0 <= nr < len(board)
            and 0 <= nc < len(board[0])
            and board[nr][nc] not in visit
        ):
            dfs(nr, nc)
    visit.remove(board[r][c])


dfs(0, 0)
print(cnt)
