# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_seen = -1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one_seen <= k and last_one_seen != -1:
                    return False
                last_one_seen = i
        return True

