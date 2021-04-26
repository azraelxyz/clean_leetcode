# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        possible_sets = self.subsets(nums[:-1])
        return possible_sets + [[nums[-1]] + _set for _set in possible_sets]

