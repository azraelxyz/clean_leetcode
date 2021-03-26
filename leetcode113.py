# https://leetcode.com/problems/path-sum-ii/

class Solution:
    def __init__(self):
        self._ans = []

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        currentSum = 0
        currentTraverse = []
        self.dfs(root, currentSum, targetSum, currentTraverse)
        return self._ans

    def dfs(self, root, parentSum, targetSum, currentTraverse):
        currentSum = parentSum + root.val
        currentTraverse.append(root.val)
        if root.left is None and root.right is None:
            if currentSum == targetSum:
                self._ans.append(currentTraverse)

        if root.left:
            self.dfs(root.left, currentSum, targetSum, list(currentTraverse))
        if root.right:
            self.dfs(root.right, currentSum, targetSum, list(currentTraverse))

