# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if len(strs) == 0:
            return common_prefix

        common_prefix = strs[0]
        for str in strs[1:]:
            common_prefix = self._find_common_prefix(str, common_prefix)
        return common_prefix

    def _find_common_prefix(self, str1, str2):
        common_prefix_index = 0
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                common_prefix_index += 1
            else:
                break
        return str1[:common_prefix_index]

