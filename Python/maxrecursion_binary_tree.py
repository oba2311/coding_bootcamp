# construct a tree:

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = Node([10,3,5])

root.PrintTree()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# tree = [1, 2, 3, None, None, 4, 5, 6]
#
# class Solution:
#     """Docstring."""
#
#     def __init__(self, tree_as_a_list):
#         self.val = tree_as_a_list
#         self.left = None
#         self.right = None
#
#
#     def maxDepth(self, root):
#         """Docstring."""
#         if root is None:
#             return 0
#         right = Solution.maxDepth(self, root.right)
#         left = Solution.maxDepth(self, root.left)
#         return max(right, left)+1
#
# # iterative solution:
#
#
#
# s = Solution(tree)
# depth = s.maxDepth(tree)
# print(depth)
