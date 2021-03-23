# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        remaining_s = s
        for char in t:
            if len(remaining_s) > 0 and char == remaining_s[0]:
                remaining_s = remaining_s[1:]
        return len(remaining_s) == 0

