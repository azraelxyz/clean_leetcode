# https://leetcode.com/problems/roman-to-integer/

class Solution:
    MAPPING = {
        'I':    1,
        'IV':   4,
        'V':    5,
        'IX':   9,
        'X':   10,
        'XL':  40,
        'L':   50,
        'XC':  90,
        'C':  100,
        'CD': 400,
        'D':  500,
        'CM': 900,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        i = 0
        _sum = 0
        while i < len(s):
            if s[i:i+2] in self.MAPPING:
                roman = s[i:i+2]
                i = i + 2
            else:
                roman = s[i]
                i = i + 1
            _sum += self.MAPPING[roman]
            print(roman, _sum)

        return _sum

