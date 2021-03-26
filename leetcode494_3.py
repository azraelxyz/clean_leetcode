# https://leetcode.com/problems/target-sum/

# defaultdict + dp solution

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = sum(nums)
        if max_sum < S:
            return 0
        dp = defaultdict(lambda: defaultdict(int))
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i, num in enumerate(nums[1:]):
            for possible_sum in range(-max_sum, max_sum+1):
                dp[i+1][possible_sum] += dp[i][possible_sum+num]
                dp[i+1][possible_sum] += dp[i][possible_sum-num]

        return dp[len(nums)-1][S]

