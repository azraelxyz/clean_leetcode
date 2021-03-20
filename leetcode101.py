# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS approach

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        current_level_nodes =[root]
        
        while len(current_level_nodes) > 0:
            if self.is_all_none(current_level_nodes):
                break
            if self.is_symmetric_level(current_level_nodes) is False:
                return False

            next_level_nodes = []
            for node in current_level_nodes:
                if node:
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
        return True
    
    def is_symmetric_level(self, level_nodes) -> bool:
        values = []
        n = len(level_nodes)
        for i in range(n):
            left_node = level_nodes[i]
            right_node = level_nodes[n-i-1]
            if left_node is None and right_node is not None:
                return False
            if left_node is not None and right_node is None:
                return False
            if left_node and right_node and left_node.val != right_node.val:
                return False
        return True
    
    def is_all_none(self, level_nodes) -> bool:
        for node in level_nodes:
            if node is not None:
                return False
        return True

