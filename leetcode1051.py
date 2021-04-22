# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                count += 1
        return count

