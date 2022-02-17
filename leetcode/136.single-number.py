#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for i in dic:
            if dic[i] == 1:
                return i


# @lc code=end
