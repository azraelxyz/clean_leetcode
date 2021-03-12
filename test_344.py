import pytest

from leetcode344 import Solution

@pytest.mark.parametrize("s,expected", [
    ([], []),
    (["a"], ["a"]),
    (["a", "b", "c"], ["c", "b", "a"]),
    (["a", "b", "c", "d"], ["d", "c", "b", "a"]),
])
def testSolutionReverseString(s, expected):
    assert Solution().reverseString(s) == expected
