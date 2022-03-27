from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):

        cnt = Counter(comb)

        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10 - i] < cnt[i]:
                score1 += i
            elif info[10 - i] > 0:
                score2 += i

        diff = score1 - score2
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff

    if max_diff > 0:
        answer = [0] * 11
        for n in max_comb_cnt:
            answer[10 - n] = max_comb_cnt[n]
        return answer
    else:
        return [-1]


from copy import deepcopy

max_diff, max_board = 0, []


def solution(n, info):
    def dfs(ascore, lscore, cnt, idx, board):
        global max_diff, max_board
        if cnt > n:
            return
        if idx > 10:
            diff = lscore - ascore
            if diff > max_diff:
                board[10] = n - cnt
                max_board = board
                max_diff = diff
            return
        if cnt < n:
            board2 = deepcopy(board)
            board2[10 - idx] = info[10 - idx] + 1
            dfs(ascore, lscore + idx, cnt + info[10 - idx] + 1, idx + 1, board2)

        board1 = deepcopy(board)

        if info[10 - idx] > 0:
            dfs(ascore + idx, lscore, cnt, idx + 1, board1)
        else:
            dfs(ascore, lscore, cnt, idx + 1, board1)

    dfs(0, 0, 0, 0, [0] * 11)
    return max_board if max_board else [-1]
