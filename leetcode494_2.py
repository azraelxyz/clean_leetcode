# https://leetcode.com/problems/target-sum/

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S:
            return 0
        max_sum = 1000
        min_sum = -max_sum
        dp = {}
        for i in range(0, len(nums)):
            dp[i] = defaultdict(int)

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i, num in enumerate(nums[1:]):
            for possible_sum in range(min_sum, max_sum+1):
                if possible_sum+num < max_sum+1:
                    dp[i+1][possible_sum] += dp[i][possible_sum+num]
                if possible_sum-num > min_sum-1:
                    dp[i+1][possible_sum] += dp[i][possible_sum-num]

        return dp[len(nums)-1][S]

