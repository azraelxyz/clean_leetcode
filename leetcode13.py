# https://leetcode.com/problems/roman-to-integer/

class Solution:
    MAPPING = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    REPLACEMENT = {
        'IV': 'IIII',
        'IX': 'VIIII',
        'XL': 'XXXX',
        'XC': 'LXXXX',
        'CD': 'CCCC',
        'CM': 'DCCCC'
    }
    def romanToInt(self, s: str) -> int:
        replaced_string = s
        for key, value in self.REPLACEMENT.items():
            replaced_string = replaced_string.replace(key, value)

        _sum = 0
        for char in replaced_string:
            _sum += self.MAPPING[char]

        return _sum

