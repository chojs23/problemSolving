def solution(m, n, board):
    answer = 0
    board = [[]]

    def isSquare(r, c):
        if r >= m - 1 or c >= n - 1:
            return False
        char = board[r][c]

        if board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] == char:
            return True
        return False

    temp = []
    for i in range(m):
        for j in range(n):
            if isSquare(i, j):
                temp.append((i, j))
    for t in temp:
        r, c = t[0], t[1]
        board[r][c] = "."
        board[r + 1][c] = "."
        board[r][c + 1] = "."
        board[r + 1][c + 1] = "."

    print(board)
    return answer
