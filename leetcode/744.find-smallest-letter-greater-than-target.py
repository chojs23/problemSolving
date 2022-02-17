#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if n == 0:
            return None

        low = 0
        high = n - 1
        # If it can not be found, must be the first element (wrap around)
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[result]


# @lc code=end
