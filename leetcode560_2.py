# https://leetcode.com/problems/subarray-sum-equals-k/

# hashmap solution

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, _sum = 0, 0
        hashmap = {0: 1}
        for i in range(len(nums)):
            _sum += nums[i]
            if hashmap.get(_sum-k):
                count += hashmap.get(_sum-k)
            hashmap[_sum] = hashmap.get(_sum, 0) + 1

        return count

