#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq


class MedianFinder(object):
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0]) > self.large[0]:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) == len(self.large):
            return (float)(-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
