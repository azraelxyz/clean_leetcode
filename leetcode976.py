# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums = sorted(nums, reverse=True)
        for i in range(0, len(nums)-2):
            if nums[i+2] + nums[i+1] > nums[i]:
                return  nums[i+2] +  nums[i+1] + nums[i]
        return 0

