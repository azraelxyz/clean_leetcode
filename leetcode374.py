# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.binarySearch(0, n)

    def binarySearch(self, start, end):
        i = (end + start) // 2
        if i == start:
            i = i + 1
        if guess(i) == 0:
            return i
        elif guess(i) == 1:
            return self.binarySearch(i, end)
        elif guess(i) == -1:
            return self.binarySearch(start, i)

