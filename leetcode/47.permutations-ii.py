# @before-stub-for-debug-begin
from python3problem47 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()

        dfs()

        return res


# @lc code=end
