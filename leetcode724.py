# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suffixSum = sum(nums)
        prefixSum = 0
        pivotIndex = -1
        for i, num in enumerate(nums):
            suffixSum -= num
            if prefixSum == suffixSum:
                pivotIndex = i
                break
            prefixSum += num
        return pivotIndex

