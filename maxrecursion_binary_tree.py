# workable with Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        right = Solution.maxDepth(self,root.right)
        left = Solution.maxDepth(self,root.left)
        return max(right,left)+1
