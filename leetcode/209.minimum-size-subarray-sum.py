# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        res = len(nums) + 1
        total = 0
        for right, n in enumerate(nums):
            total += n
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return res if res != len(nums) + 1 else 0


# @lc code=end
