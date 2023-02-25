# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        _sum, parts = 0, 0
        for x in arr:
            _sum += x
            if 3 * _sum == total:
                _sum = 0
                parts += 1
        return parts >= 3
