#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        answer = []
        dic = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}
        for word in words:

            f, s, t = 0, 0, 0
            for i in word:
                if i.lower() in dic[1]:
                    f += 1
                if i.lower() in dic[2]:
                    s += 1
                if i.lower() in dic[3]:
                    t += 1
            if f == len(word) or s == len(word) or t == len(word):
                answer.append(word)
        return answer


# @lc code=end
