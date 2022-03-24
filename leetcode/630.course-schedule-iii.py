#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
import heapq

# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        start = 0
        courses = sorted(courses, key=lambda x: x[1])
        for t, end in courses:
            start += t
            heapq.heappush(pq, -t)
            if start > end:
                start += heapq.heappop(pq)
        return len(pq)


# @lc code=end
