# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = {}
        for num in A:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] == len(A)/2:
                return num

