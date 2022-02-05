#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, targetSum)]
        while stack:
            node, _sum = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                return True
            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))
        return False


# @lc code=end
