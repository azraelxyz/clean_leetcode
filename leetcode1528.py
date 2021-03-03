# https://leetcode.com/problems/shuffle-string/
class Solution:
    def restoreString(self, s, indices) -> str:
        x = [None] * len(indices)
        for i, j in enumerate(indices):
            x[j] = s[i]
        return ''.join(x)
