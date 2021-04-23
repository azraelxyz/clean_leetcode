# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = set([i for i in range(n+1)])
        diff = expected - set(nums)
        return diff.pop()

