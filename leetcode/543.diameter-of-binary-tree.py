#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def depth(root):
            if not root:
                return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best


# @lc code=end
