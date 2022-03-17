# @before-stub-for-debug-begin
from python3problem437 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, prevSum, targetsum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - targetsum in rec:
                count += rec[currSum - targetsum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, targetsum)
            count += dfs(root.right, currSum, targetsum)
            rec[currSum] -= 1
            return count

        rec = {0: 1}
        return dfs(root, 0, targetSum)


# @lc code=end
