# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        maxHead = self.buildMaxHead(height)
        maxTail = self.buildMaxTail(height)

        count = 0
        for i in range(1, len(height)-1):
            candidate = min(maxHead[i-1], maxTail[i+1])
            count += max(candidate - height[i], 0)
        return count

    def buildMaxHead(self, height):
        _max = 0
        maxHead = {}
        for i in range(0, len(height)):
            _max = max(_max, height[i])
            maxHead[i] = _max
        return maxHead
    
    def buildMaxTail(self, height):
        _max = 0
        maxTail = {}
        for i in range(len(height) - 1, 0, -1):
            _max = max(_max, height[i])
            maxTail[i] = _max
        return maxTail

