import pytest

from leetcode560 import Solution

@pytest.mark.parametrize("nums,k,expected", [
    ([], 3, 0),
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
    ([-1,-1,1], 0, 1),
])
def testSolutionSubarraySum(nums, k, expected):
    assert Solution().subarraySum(nums, k) == expected
