# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = self.arrayToInt(digits)
        answer = num + 1
        return self.intToArray(answer)

    def arrayToInt(self, digits):
        max_level = len(digits) - 1
        num = 0
        for i, digit in enumerate(digits):
            level =  max_level-i
            base = pow(10, level)
            num += base * digit
        return num

    def intToArray(self, num):
        output = []
        while True:
            tail_digit= num % 10
            output.insert(0, tail_digit)
            num = num // 10
            if num == 0:
                return output

