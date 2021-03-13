# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        hash_map = self._build_hash_map(nums1)
        return self._lookup_hash_map(nums2, hash_map)

    def _build_hash_map(self, nums): # time complexity: O(n), where n is len(nums).
        hash_map = {}
        for num in nums:
            hash_map[num] = 1
        return hash_map

    def _lookup_hash_map(self, nums, hash_map): # time complexity: O(n), where n is len(nums).
        ret = set()
        for num in nums:
            if hash_map.get(num):
                ret.add(num)
        return ret

