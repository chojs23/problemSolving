#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        prev = None
        heap = []
        c = Counter(s)
        heap = [(-val, key) for key, val in c.items()]
        heapq.heapify(heap)
        while heap or prev:
            if prev and not heap:
                return ""
            cnt, char = heapq.heappop(heap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)

        return res


# @lc code=end
