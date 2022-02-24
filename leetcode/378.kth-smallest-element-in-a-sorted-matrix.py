#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from bisect import bisect_right
from heapq import heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(m):
            cnt = 0
            for row in range(n):
                x = bisect_right(matrix[row], m)
                cnt += x
            return cnt

        while l < r:
            mid = (l + r) // 2
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid

        return l


# @lc code=end
