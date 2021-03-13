import pytest

from leetcode14 import Solution

@pytest.mark.parametrize("str1,str2,expected", [
    ( "abcdefghi", "abcdoooooo", "abcd"),
    ( "", "abcdoooooo", ""),
    ( "abcdefghi", "", ""),
    ( "abcdefghi", "a", "a"),
])
def testSolutionFindCommonPrefix(str1, str2, expected):
    assert Solution()._find_common_prefix(str1, str2) == expected
