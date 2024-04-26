# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        values = []
        for num in nums:
            if num != 0:
                values.append(num)

        for i, value in enumerate(values):
            nums[i] = value

        for i in range(len(values), len(nums)):
            nums[i] = 0

