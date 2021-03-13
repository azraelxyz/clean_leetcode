import pytest

from leetcode33_3 import Solution

@pytest.mark.parametrize("nums,target,expected", [
    ([5, 1, 3], 5, 0),
])
def testSolutionSearch(nums, target, expected):
    assert Solution().search(nums, target) == expected

@pytest.mark.parametrize("nums,expected", [
    ([5, 1, 3], 1),
])
def testSolutionFindPivot(nums, expected):
    assert Solution()._find_pivot(nums) == expected
