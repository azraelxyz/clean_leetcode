# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = {}
        for num in A:
            if counter.get(num) == True:
                return num
            counter[num] = True

