# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        x = 0
        for n in nums:
            x += n
            output.append(x)
        return output
