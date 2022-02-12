# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        s = []
        n = len(candidates)

        def dfs(start):
            if sum(s) > target:
                return

            if sum(s) == target:
                res.append(s[:])
                return

            for i in range(start, n):
                s.append(candidates[i])
                dfs(i)
                s.pop()

        dfs(0)
        return res


# @lc code=end
