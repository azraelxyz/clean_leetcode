# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        hash_map = {}
        for num in nums:
            if hash_map.get(num):
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for i, v in hash_map.items():
            if v > majority:
                return i
