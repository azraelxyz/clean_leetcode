# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = ''.join(sorted(s))
            if result.get(key) is not None:
                result[key].append(s)
            else:
                result[key] = [s]
        return result.values()

