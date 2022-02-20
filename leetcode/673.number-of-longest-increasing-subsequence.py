# @before-stub-for-debug-begin
from operator import length_hint
from python3problem673 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}  # key =index, value=[length of LIS,count]
        lenLIS, res = 0, 0

        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count

            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

            dp[i] = [maxLen, maxCnt]

        return res


# @lc code=end
