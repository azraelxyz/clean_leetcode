# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = int(len(nums)/2)
        output = []
        first_array = nums[0:n]
        second_array = nums[n:2*n]

        for i in range(n):
            output.append(first_array[i])
            output.append(second_array[i])

        return output
