#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        start = intervals[0][0]
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] == start:
                res += 1
                last = intervals[i][1]
            elif last > intervals[i][0] > start and intervals[i][1] > last:
                res += 1
            elif last > intervals[i][0] > start and intervals[i][1] <= last:
                res += 1
                start = intervals[i][0]
                last = intervals[i][1]
            else:
                start = intervals[i][0]
                last = intervals[i][1]

        return res


# @lc code=end
