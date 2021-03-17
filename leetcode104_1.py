# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_height = 1+ self.maxDepth(root.left)
        right_height = 1+ self.maxDepth(root.right)
        return max(left_height, right_height)

