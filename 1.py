n = int(input())

board = [list(map(str, input())) for _ in range(n)]
res = 0


def check():
    cnt = 0

    for i in range(n):
        max_col = 1
        max_row = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                max_row += 1
            else:
                cnt = max(max_row, cnt)
                max_row = 1
            if board[j][i] == board[j + 1][i]:
                max_col += 1
            else:
                cnt = max(max_col, cnt)
                max_col = 1
        cnt = max(cnt, max_row, max_col)
    return cnt


for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            tmp = board[i][j]
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = tmp

            res = max(res, check())

            tmp = board[i][j]
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = tmp

        if board[j][i] != board[j + 1][i]:
            tmp = board[j][i]
            board[j][i] = board[j + 1][i]
            board[j + 1][i] = tmp

            res = max(res, check())

            tmp = board[j][i]
            board[j][i] = board[j + 1][i]
            board[j + 1][i] = tmp

print(res)
