#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if not r:
            return 0

        while l <= r:
            m = (l + r) // 2

            if not m == len(nums) - 1 and nums[m] > nums[m + 1]:
                if nums[m - 1] < nums[m]:
                    return m
                r = m - 1
            else:
                l = m + 1

        return m


# @lc code=end
