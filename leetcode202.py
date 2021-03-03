# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            nextN = self.sumOfSquares(n)
            if nextN == 1:
                return True
            elif nextN in visited:
                return False
            else:
                visited.add(n)
                n = nextN
        
    def sumOfSquares(self, n):
        if n == 0:
            return 0
        return (n % 10) ** 2 + self.sumOfSquares(n//10)

s = Solution()
print(s.isHappy(2))
