# https://leetcode.com/problems/deepest-leaves-sum/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        height = self.getHeight(root)
        return self.getSum(root, 1, height)

    def getHeight(self, root: TreeNode) -> int:
        node = root
        if node.left is None and node.right is None:
            return 1
        elif node.left and node.right:
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        elif node.left and node.right is None:
            return self.getHeight(node.left) + 1
        elif node.left is None and node.right:
            return self.getHeight(node.right) + 1

    def getSum(self, root: TreeNode, level, height) -> int:
        node = root
        if node.left is None and node.right is None:
            if level == height:
                return node.val
            else:
                return 0
        elif node.left and node.right:
            return self.getSum(node.left, level+1, height) + self.getSum(node.right, level+1, height)
        elif node.left and node.right is None:
            return self.getSum(node.left, level+1, height)
        elif node.left is None and node.right:
            return self.getSum(node.right, level+1, height)
