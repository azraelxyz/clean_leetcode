# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        ret = ''
        if n == 1:
            ret = '1'
        else:
            ret = self.RLE(self.countAndSay(n-1))
        return ret

    def RLE(self, chars: str):
        if len(chars) == 0:
            return ''

        s = ''
        count = 0
        prev_char = ''
        for i, char in enumerate(chars):
            if prev_char != char:
                if count > 0:
                    s += str(count)
                    s += prev_char
                prev_char = char
                count = 0
            count += 1
        if count > 0:
            s += str(count)
            s += prev_char
        return s

