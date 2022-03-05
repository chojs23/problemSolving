#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[m][0]:  # target's row is smaller than row m
                r = m - 1
            elif target > matrix[m][-1]:  # target's row is larger than row m
                l = m + 1
            else:  # target is in row m
                break
        if target in matrix[m]:
            return True


# @lc code=end
