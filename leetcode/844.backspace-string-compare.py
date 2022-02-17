#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rs = 0
        rt = 0
        while 0 <= rs < len(s):
            if s[rs] == "#" and rs == 0:
                s = s[rs + 1 :]
                rs -= 1
            elif s[rs] == "#":
                s = s[: rs - 1] + s[rs + 1 :]
                rs -= 2
            rs += 1

        while 0 <= rt < len(t):
            if t[rt] == "#" and rt == 0:
                t = t[rt + 1 :]
                rt -= 1
            elif t[rt] == "#":
                t = t[: rt - 1] + t[rt + 1 :]
                rt -= 2
            rt += 1

        if s == t:
            return True


# @lc code=end
