# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _max = 0
        at = 0
        for g in gain:
            at = at + g
            _max = max(at, _max)
        return _max

