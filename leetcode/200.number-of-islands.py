#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        n = len(grid)
        m = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != "1":
                return
            grid[r][c] = 0

            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                dfs(nr, nc)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


# @lc code=end
