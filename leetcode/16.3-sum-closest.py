#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        best_s = 100000
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                s = nums[l] + nums[r] + num
                if s == target:
                    return s

                if abs(target - s) < abs(target - best_s):
                    best_s = s

                if s <= target:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                else:
                    r -= 1

        return best_s


# @lc code=end
