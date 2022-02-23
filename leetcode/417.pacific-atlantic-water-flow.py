# @before-stub-for-debug-begin
from python3problem417 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque


class Solution:
    def pacificAtlantic(self, M: List[List[int]]) -> List[List[int]]:

        m = len(M)
        n = len(M[0])
        nx = [0, 0, 1, -1]
        ny = [1, -1, 0, 0]

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    dy, dx = y + ny[i], x + nx[i]
                    if (
                        0 <= dx < m
                        and 0 <= dy < n
                        and (dx, dy) not in visited
                        and M[dx][dy] >= M[x][y]
                    ):
                        queue.append((dx, dy))
                        visited.add((dx, dy))

            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m)]

        return bfs(pacific) & bfs(atlantic)


# @lc code=end
