#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = set(s)
        # print(s)
        s = sorted(s)
        return "".join(s)


# @lc code=end
