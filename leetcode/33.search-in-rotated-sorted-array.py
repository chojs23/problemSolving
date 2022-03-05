# @before-stub-for-debug-begin
from python3problem33 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


# @lc code=end
