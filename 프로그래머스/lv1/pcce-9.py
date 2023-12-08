# BFS
import collections


def solution(board, h, w):
    answer = 0

    answer = bfs(board, h, w)
    return answer


def bfs(board, r, c):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = collections.deque()
    q.append((r, c))
    result = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (
                0 <= nr < len(board)
                and 0 <= nc < len(board[0])
                and board[nr][nc] == board[r][c]
            ):
                result += 1

    return result


# test code

board = [
    ["blue", "red", "orange", "red"],
    ["red", "red", "blue", "orange"],
    ["blue", "orange", "red", "red"],
    ["orange", "orange", "red", "blue"],
]
h = 1
w = 1

print(solution(board, h, w))
