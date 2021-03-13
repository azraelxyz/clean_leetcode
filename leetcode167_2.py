# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                return [left + 1, right + 1] # 1-indexed
            elif _sum < target:
                left = left + 1
            else:
                right = right - 1

