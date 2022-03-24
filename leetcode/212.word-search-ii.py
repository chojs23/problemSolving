#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        row, col = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):

            if (
                r < 0
                or c < 0
                or r == row
                or c == col
                or board[r][c] not in node.children
                or (r, c) in visit
            ):
                return
            if not node.children[board[r][c]]:
                del node.children[board[r][c]]
            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for i in range(row):
            for j in range(col):
                dfs(i, j, root, "")

        return list(res)


# @lc code=end
