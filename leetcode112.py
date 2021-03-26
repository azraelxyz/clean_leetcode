# https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        currentSum = 0
        return self.dfs(root, currentSum, targetSum)
        
    def dfs(self, root, parentSum, targetSum):
        currentSum = parentSum + root.val
        if root.left is None and root.right is None:
            if currentSum == targetSum:
                return True
            else:
                return False

        left_result = right_result = False
        if root.left:
            left_result = self.dfs(root.left, currentSum, targetSum)
        if root.right:
            right_result = self.dfs(root.right, currentSum, targetSum)
        return left_result or right_result

