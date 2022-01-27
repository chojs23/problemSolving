#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for val in dic.values():
            if val != 1:
                return True

        return False

        # @lc code=end
