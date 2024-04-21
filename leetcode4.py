# https://leetcode.com/problems/median-of-two-sorted-arrays/

# O(nlogn) solution with merge sort

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.mergeSorted(nums1, nums2)
        return self.medium(merged)

    def medium(self, nums):
        x = len(nums)
        if x % 2 == 0:
            medium = (nums[x//2] + nums[x//2-1])/2
        else:
            medium = nums[x//2]
        return medium

    def mergeSorted(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        merged = []
        j = k = 0
        for i in range(m+n):
            if k >= n:
                merged.append(nums1[j])
                j = j + 1
                continue
            if j >= m:
                merged.append(nums2[k])
                k = k + 1
                continue
            if nums1[j] >= nums2[k]:
                merged.append(nums2[k])
                k = k + 1
            else:
                merged.append(nums1[j])
                j = j + 1
        return merged

