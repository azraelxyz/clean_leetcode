import pytest

from leetcode347 import Solution

@pytest.mark.parametrize("nums,k,expected",[
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([7, 7, 7, 7, 2, 2, 2], 1, [7])
])
def testTopKFrequent(nums, k, expected):
    solution = Solution()
    assert solution.topKFrequent(nums, k) == expected
