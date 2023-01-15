from bisect import bisect, bisect_right, bisect_left, insort_left

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        sliding_window = []
        for i in range(len(nums)):
            if i > indexDiff: sliding_window.remove(nums[i-indexDiff-1])

            floor_index = self.find_rightmost_le(sliding_window, nums[i])
            ceil_index = self.find_leftmost_ge(sliding_window, nums[i])
            if floor_index is not None:
                if abs(nums[i] - sliding_window[floor_index]) <= valueDiff:
                    return True
            if ceil_index is not None:
                if abs(nums[i] - sliding_window[ceil_index]) <= valueDiff:
                    return True
            insort_left(sliding_window, nums[i])

        return False

    def find_rightmost_le(self, a, x):
        i = bisect_right(a, x)
        if i:
            return i-1
        return None

    def find_leftmost_ge(self, a, x):
        i = bisect_left(a, x)
        if i != len(a):
            return i
        return None
