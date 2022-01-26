#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
import bisect


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1  # deal with exception
        l, r = 0, x

        while l <= r:
            mid = (r + l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


# @lc code=end
