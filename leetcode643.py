# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = sum(nums[0:k])
        _max = _sum
        for i in range(1, len(nums)-k+1):
            _sum = _sum - nums[i-1] + nums[i+k-1]
            if _max < _sum:
                _max = _sum
        return _max / k

