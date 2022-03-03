#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        ans, arrow = 0, 0
        for [start, end] in points:
            if ans == 0 or start > arrow:
                ans, arrow = ans + 1, end
        return ans


# @lc code=end
