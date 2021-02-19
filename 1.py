# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, j in enumerate(nums):
            hash_map[j] = i

        for i, j in enumerate(nums):
            x = hash_map.get(target-j)
            if x is not None and i != x:
                return i, x
