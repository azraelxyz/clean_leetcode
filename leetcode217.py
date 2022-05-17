class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _dict = {}
        for num in nums:
            if num in _dict.keys():
                _dict[num] += 1
            else:
                _dict[num] = 1
        for value in _dict.values():
            if value > 1:
                return True
        return False
