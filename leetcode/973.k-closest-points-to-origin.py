#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: (x[1] ** 2) + (x[0] ** 2))
        res = []
        print(points)
        for i in range(k):
            res.append(points[i])

        return res


# @lc code=end
