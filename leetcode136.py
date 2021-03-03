# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            value = visited.get(num, 0)
            visited[num] = value + 1
        for num, value in visited.items():
            if value == 1:
                return num
