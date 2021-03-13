# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return (-1, -1)

        index = self._binary_search(nums, 0, len(nums)-1, target)
        if index == -1:
            return (-1, -1)

        first_position, last_position = index, index
        for i in range(index, len(nums)):
            if nums[i] != target:
                break
            last_position = i

        for i in range(index, -1, -1):
            if nums[i] != target:
                break
            first_position = i

        return (first_position, last_position)

    def _binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self._binary_search(nums, left, mid-1, target)
        elif nums[mid] < target:
            return self._binary_search(nums, mid+1, right, target)

