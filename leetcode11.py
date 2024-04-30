# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        _max = self.calculateArea(left, right, height)

        while True:
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
            area = self.calculateArea(left, right, height)
            _max = max(_max, area)
            if left >= right:
                break

        return _max

    @staticmethod
    def calculateArea(left, right, height):
        h = min(height[left], height[right])
        area = h * (right-left)
        return area
