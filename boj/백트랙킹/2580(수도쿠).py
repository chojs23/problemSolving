import sys

input = sys.stdin.readline


board = []


def findUnassigned():
    for row in range(9):
        for col in range(9):
            if board[row][col] == "0":
                return row, col
    return -1, -1


def checkrow(row, ch):
    for col in range(9):
        if board[row][col] == ch:
            return False
    return True


def checkcol(col, ch):
    for row in range(9):
        if board[row][col] == ch:
            return False
    return True


def checksquare(row, col, ch):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if board[r][c] == ch:
                return False
    return True


def isSafe(row, col, ch):
    boxrow = row - row % 3
    boxcol = col - col % 3
    if checkrow(row, ch) and checkcol(col, ch) and checksquare(boxrow, boxcol, ch):
        return True
    return False


for i in range(9):
    board.append(list(input().rstrip().split()))


def solve():
    r, c = findUnassigned()

    if r == -1 and c == -1:
        return True
    for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if isSafe(r, c, num):
            board[r][c] = num
            if solve():
                return True
            board[r][c] = "0"
    return False


solve()

for r in board:
    print(" ".join(r))
