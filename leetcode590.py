# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

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

    def postorder(self, root: 'Node') -> List[int]:
        if root is not None:
            for node in root.children:
                self.postorder(node)
            self.output.append(root.val)
        return self.output

