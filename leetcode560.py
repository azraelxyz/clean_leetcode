# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

# time complexity is O(n^2) and it will be Time Limit Exceeded

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum = sum + nums[end]
                if sum == k:
                    count += 1

        return count
