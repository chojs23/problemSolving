# @before-stub-for-debug-begin
from python3problem216 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        cur = []

        def dfs(start, idx):
            if idx == k and sum(cur) == n:
                res.append(cur[:])
                return
            if sum(cur) > n or idx > k:
                return

            for i in range(start, 10):
                if sum(cur + [i]) > n:
                    continue
                cur.append(i)
                dfs(i + 1, idx + 1)
                cur.pop()

        dfs(1, 0)

        return res


# @lc code=end
