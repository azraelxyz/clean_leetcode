# https://leetcode.com/problems/maximum-subarray/

import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        _max = -math.inf
        _sum = 0
        for num in nums:
            _sum += num
            if _sum > _max:
                _max = _sum
            if _sum < 0:
                _sum = 0

        return _max
