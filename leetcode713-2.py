# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int: 
        start, end, count = 0, 0, 0
        production = 1
        while end < len(nums):
            production *= nums[end]
            while production >= k and start <= end:
                production = production / nums[start]
                start += 1
            count += (end - start + 1)
            end += 1
        return count
