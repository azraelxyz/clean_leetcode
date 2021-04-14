# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        pointer = 0
        for i, num in enumerate(nums):
            if nums[pointer] != num:
                pointer += 1
                nums[pointer] = num
        nums = nums[:pointer+1]
        return len(nums)

