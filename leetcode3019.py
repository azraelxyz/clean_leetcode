# https://leetcode.com/problems/number-of-changing-keys/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        if len(s) == 0:
            return count

        last_seen = s[0].lower()
        for i in range(1, len(s)):
            current = s[i].lower()
            if current != last_seen:
                count += 1
                last_seen = current
        return count

