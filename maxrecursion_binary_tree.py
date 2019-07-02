# workable with Leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


tree = [1,2,3,null,null,4,5,6]

class Solution:
    """Docstring."""

    def maxDepth(self, root):
        """Docstring."""
        if root is None:
            return 0
        right = Solution.maxDepth(self, root.right)
        left = Solution.maxDepth(self, root.left)
        return max(right, left)+1

# iterative solution:



s = Solution()
depth = s.maxDepth(tree)
print(depth)
