# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        current_level_nodes = [root]
        output = []
        while current_level_nodes:
            next_level_nodes = []
            current_level_values = []
            for node in current_level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
                current_level_values.append(node.val)
            output.append(current_level_values)
            current_level_nodes = next_level_nodes
        return output

