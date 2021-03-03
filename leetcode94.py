# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output_values = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.output_values
    
    def inorder(self, node: TreeNode) -> int:
        if node is not None:
            self.inorder(node.left)
            self.output_values.append(node.val)
            self.inorder(node.right)
