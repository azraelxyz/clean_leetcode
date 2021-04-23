# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        upper, lower = n+1, 0
        expected = n*(upper+lower)//2
        actual = sum(nums)
        return expected - actual

