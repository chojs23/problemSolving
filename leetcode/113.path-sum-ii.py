#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path):
            if not node:
                return

            # print(path)
            if sum(path) == targetSum and not (node.left or node.right):
                res.append(path.copy())
                return
            if node.left:
                dfs(node.left, path + [node.left.val])

            if node.right:
                dfs(node.right, path + [node.right.val])

        if root:
            dfs(root, [root.val])
        else:
            return []
        return res


# @lc code=end
