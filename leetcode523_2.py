# https://leetcode.com/problems/continuous-subarray-sum/

# prefix sum + hashmap approach

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_before = self.build_sum_before(nums)

        hashmap = {}
        hashmap[0] = -1
        for i in range(len(nums)):
            if k != 0:
                _sum = sum_before[i] % k
            if _sum in hashmap and i - hashmap[_sum] > 1:
                return True
            if _sum not in hashmap:
                hashmap[_sum] = i
        return False
        
    def build_sum_before(self, nums):
        sum_before = {}
        sum_before[-1] = 0
        for i, num in enumerate(nums):
            sum_before[i] = sum_before[i-1] + num
        return sum_before

