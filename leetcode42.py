# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxHeight = max(height)
        count = 0
        _max = 0

        maxHead = {}
        for i in range(0, n):
            _max = max(_max, height[i])
            maxHead[i] = _max

        _max = 0
        maxTail = {}
        for i in range(n-1, 0, -1):
            _max = max(_max, height[i])
            maxTail[i] = _max

        for i in range(1, n-1):
            candidate = min(maxHead[i-1], maxTail[i+1])
            count += max(candidate - height[i], 0)
        return count

