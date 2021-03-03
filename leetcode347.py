# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = self.buildHashMap(nums)
        k_th_largest_value = self.findTheKLargestValue(list(hash_map.values()), k)
        
        output = []
        for key, value in hash_map.items():
            if value >= k_th_largest_value:
                output.append(key)
        return output
        
    def buildHashMap(self, nums: List[int]) -> dict:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return hash_map
            
    def findTheKLargestValue(self, values: List[int], k: int) -> int:
        # Time complexity: O(nlogn)
        # A better way is using heap to implement this function
        return sorted(values, reverse=True)[k-1]
