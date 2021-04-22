# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.output = []

    def preorder(self, root: 'Node') -> List[int]:
        if root is not None:
            self.output.append(root.val)
            for node in root.children:
                self.preorder(node)
        return self.output

