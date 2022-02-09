#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] = -1 * nums[abs(num) - 1]

        return result


# @lc code=end
