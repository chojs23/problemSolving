#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n != len(original):
            return res

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[i * n + j])
            res.append(temp)

        return res


# @lc code=end
