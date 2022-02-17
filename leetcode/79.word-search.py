# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))

            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        # O(n*m*dfs times) = O(n*m*4^len(word))
        # dfs O(len(word)
        # 4^len(word)


# @lc code=end
