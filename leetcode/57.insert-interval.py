# @before-stub-for-debug-begin
from python3problem57 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)
            elif n[1] < i[0]:
                res.append(n)
                return res + intervals[index:]  # can return earlier
            else:  # overlap case
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        res.append(n)
        return res


# @lc code=end
