# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        sumset = set()
        sumset.add(0)
        for num in nums:
            temp = set()
            for i in sumset:
                temp.add(i + num)
            sumset = sumset.union(temp)
            if target in sumset:
                return True
        return False


# @lc code=end
