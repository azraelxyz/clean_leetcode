# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# hash map approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = self._build_hash_map(numbers)
        for i in range(len(numbers)):
            value = target - numbers[i]
            if hash_map.get(value) is not None:
                return [i+1, hash_map[value]+1]


    def _build_hash_map(self, numbers):
        hash_map = {}
        for i, num in enumerate(numbers):
            hash_map[num] = i
        return hash_map

