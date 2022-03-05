#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False
        h, w = len(matrix), len(matrix[0])

        # Start adaptive search from bottom left corner
        y, x = h - 1, 0

        while True:

            if y < 0 or x >= w:
                break

            current = matrix[y][x]

            if target < current:
                # target is smaller, then go up
                y -= 1

            elif target > current:
                # target is larger, then go right
                x += 1

            else:
                # hit target
                return True

        return False


# @lc code=end
