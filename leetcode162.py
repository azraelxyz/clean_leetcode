# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 0

        for i in range(len_nums):
            num = nums[i]
            if i == 0 and num > nums[i+1]:
                return i
            elif i+1 == len_nums and num > nums[i-1]:
                return i
            elif num > nums[i-1] and num > nums[i+1]:
                return i

