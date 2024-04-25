# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def __init__(self):
        self.nums = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return self.nums[n]

        for i in range(n-2):
            _next = self.nums[0] + self.nums[1] + self.nums[2]
            self.nums[0] = self.nums[1]
            self.nums[1] = self.nums[2]
            self.nums[2] = _next
        return _next

