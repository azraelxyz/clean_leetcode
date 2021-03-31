# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_map = {}
        for char in s:
            if char in counter_map:
                counter_map[char] += 1
            else:
                counter_map[char] = 1
        
        for char in t:
            if char in counter_map:
                counter_map[char] -= 1
            else:
                return False

        return all(v == 0 for v in counter_map.values())

