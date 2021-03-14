# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = {}
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            if sums[i-1] > 0:
                sums[i] = nums[i] + sums[i-1]
            else:
                sums[i] = nums[i]
        return max(sums.values())
