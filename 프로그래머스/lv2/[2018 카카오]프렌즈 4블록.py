def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    def isSquare(r, c):
        if r >= m - 1 or c >= n - 1 or board[r][c] == "." or board[r][c] == 0:
            return False
        char = board[r][c]
        if board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] == char:
            return True
        return False

    while True:
        temp = []
        for i in range(m):
            for j in range(n):
                if isSquare(i, j):
                    temp.append((i, j))
        if not temp:
            break
        for t in temp:
            r, c = t[0], t[1]
            if board[r][c] != ".":
                answer += 1
            board[r][c] = "."
            if board[r + 1][c] != ".":
                answer += 1
            board[r + 1][c] = "."
            if board[r][c + 1] != ".":
                answer += 1
            board[r][c + 1] = "."
            if board[r + 1][c + 1] != ".":
                answer += 1
            board[r + 1][c + 1] = "."

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if board[i][j] == ".":
                    x = i - 1
                    while x >= 0 and board[x][j] == ".":
                        x -= 1
                    if x < 0:
                        board[i][j] = "."
                    else:
                        board[i][j] = board[x][j]
                        board[x][j] = "."

    return answer
