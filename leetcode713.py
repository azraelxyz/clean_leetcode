# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                prod = 1
                for i in range(start, end):
                    prod *= nums[i]
                if prod < k:
                    count += 1
        return count
