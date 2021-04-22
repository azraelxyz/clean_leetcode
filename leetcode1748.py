# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_map = self.buildHashMap(nums)

        _sum = 0
        for key, value in hash_map.items():
            if value == 1:
                _sum += key
        return _sum

    def buildHashMap(self, nums):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return hash_map

