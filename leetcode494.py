# https://leetcode.com/problems/target-sum/

# brute force

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sums = {
            -1: [0]
        }

        for i, num in enumerate(nums):
            sums[i] = []
            for possible_sum in sums[i-1]:
                sums[i].append(possible_sum+num)
                sums[i].append(possible_sum-num)
            print(i, sums[i])

        count = 0
        for _sum in sums[len(nums)-1]:
            if _sum == S:
                count += 1
        return count
