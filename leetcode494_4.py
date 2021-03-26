# https://leetcode.com/problems/target-sum/

# 1-dimension dp

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = sum(nums)
        if max_sum < S:
            return 0
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1

        for i, num in enumerate(nums[1:]):
            next_dp = defaultdict(int)
            for possible_sum in dp.keys():
                next_dp[possible_sum+num] += dp[possible_sum]
                next_dp[possible_sum-num] += dp[possible_sum]
            dp = next_dp

        return dp[S]

