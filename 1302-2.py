# https://leetcode.com/problems/deepest-leaves-sum/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        while True:
            next_level_queue = []
            for node in queue:
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            if len(next_level_queue) == 0:
                return sum([n.val for n in queue])
            queue = next_level_queue

