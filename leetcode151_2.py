# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ret = ""
        word = ""
        for char in s:
            if char == " " and word != "":
                ret = word + " " + ret
                word = ""
            elif char != " ":
                word += char
        ret = word + " " + ret

        return ret.strip()

