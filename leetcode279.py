# https://leetcode.com/problems/perfect-squares/

import math

class Solution:
    def numSquares(self, n: int) -> int:
        current_level_nodes = set([n])
        count = 0

        while len(current_level_nodes):
            next_level_nodes = set()
            for node in current_level_nodes:
                if node == 0:
                    return count
                children_of_node = self.build_next_level_nodes(node)
                next_level_nodes = next_level_nodes.union(children_of_node)
            current_level_nodes = next_level_nodes
            count += 1
        return -1

    def build_next_level_nodes(self, node):
        next_level_nodes = set()
        sqrt_n = int(math.sqrt(node))
        for i in range(1, sqrt_n+1):
            required = node - i * i
            next_level_nodes.add(required)
        return next_level_nodes

