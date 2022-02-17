#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from collections import Counter


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            x = bin(i)
            ans.append(x[2:].count("1"))
        return ans


# @lc code=end
