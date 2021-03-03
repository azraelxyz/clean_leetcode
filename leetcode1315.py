# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def sumEvenGrandparent(self, root):
        queue = [root]
        sum = 0
        while True:
            next_level_queue = []
            for node in queue:
                if node.val % 2 == 0:
                    sum += self.grand_child_sum(node)
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            if len(next_level_queue) == 0:
                return sum
            queue = next_level_queue

    def grand_child_sum(self, node):
        child_left = node.left
        child_right = node.right
        sum = 0
        if child_left and child_left.left:
            sum += child_left.left.val
        if child_left and child_left.right:
            sum += child_left.right.val
        if child_right and child_right.left:
           sum += child_right.left.val
        if child_right and child_right.right:
            sum += child_right.right.val

        return sum
