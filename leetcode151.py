# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split()
        parts.reverse()
        return " ".join(parts)

