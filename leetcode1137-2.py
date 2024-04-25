# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        for _ in range(n):
            nums[0], nums[1], nums[2] = nums[1], nums[2], sum(nums)
        return nums[0]

