#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for i in s:
            tmp = []
            if i.isalpha():
                for o in res:
                    tmp.append(o + i.lower())
                    tmp.append(o + i.upper())
            else:
                for o in res:
                    tmp.append(o + i)

            res = tmp
        return res


# @lc code=end
