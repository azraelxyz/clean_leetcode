# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for char in bin(n):
            if char == "1":
                count += 1
        return count

