#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            if s == s[::-1]:

                return True
            else:
                return False

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res


# @lc code=end
