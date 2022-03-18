#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        res = 0
        prod = 1
        l, r = 0, 0
        while r < length:
            prod *= nums[r]

            while prod >= k and l < length:
                prod /= nums[l]
                l += 1
            res += r - l + 1
            r += 1

        return res if res > 0 else 0


# @lc code=end
