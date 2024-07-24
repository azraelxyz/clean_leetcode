# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = self.compress_string(chars)
        for i, char in enumerate(compressed):
            chars[i] = char
        return len(compressed)

    def compress_string(self, chars):
        s = ''
        count = 0

        for i, char in enumerate(chars):
            if i > 0:
                prev_char = chars[i-1]
            else:
                prev_char = ''

            if prev_char != char:
                if count > 1:
                    s += str(count)
                s += char
                count = 1
            else:
                count += 1
        if count > 1:
            s += str(count)
        return list(s)

