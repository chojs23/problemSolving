#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = []
        max_heap = [(-val, key) for key, val in c.items()]
        heapq.heapify(max_heap)

        while max_heap:
            for _ in range(-max_heap[0][0]):
                res.append(max_heap[0][1])
            heapq.heappop(max_heap)

        return "".join(res)


# @lc code=end
