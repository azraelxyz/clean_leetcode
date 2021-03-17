# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for row in matrix:
            for num in row:
                nums.append(num)
        return sorted(nums)[k-1]
