#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            val = target - num
            if val in hashmap:
                return [idx, hashmap[val]]
            hashmap[num] = idx
        return []


# @lc code=end
