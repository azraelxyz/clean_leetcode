# https://leetcode.com/problems/search-in-rotated-sorted-array/

# linear find pivot + binary search approach
import math

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self._find_pivot(nums)

        left, right = 0, len(nums)-1
        if nums[pivot] <= target and target <= nums[right]:
            left = pivot
        else:
            right = pivot

        return self._binary_search(nums, left, right, target)

    def _find_pivot(self, nums):
        minimum = math.inf
        min_i = 0
        for i, num in enumerate(nums):
            if minimum > num:
                minimum = num
                min_i = i
        return min_i

    def _binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

