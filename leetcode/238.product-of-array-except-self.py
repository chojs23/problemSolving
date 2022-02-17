#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]

        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] *= left
            ans[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]

        return ans


# @lc code=end
