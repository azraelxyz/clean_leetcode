import pytest

from leetcode53_2 import Solution

@pytest.mark.parametrize("nums,expected", [
    ([-1, -2, -3, -4], -1),
    ([-2, -1, -3, -4], -1),
])
def testSolutionMaxSubArray(nums, expected):
    assert Solution().maxSubArray(nums) == expected
