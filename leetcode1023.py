# https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        output = []
        for s in queries:
            ans = self.matchPattern(s, pattern)
            output.append(ans)
        return output

    def matchPattern(self, s, pattern):
        pointer_to_pattern = 0
        for char in s:
            if pointer_to_pattern >= len(pattern):
                if char.isupper():
                    return False
                else:
                    continue

            if char == pattern[pointer_to_pattern]:
                pointer_to_pattern += 1
                continue

            if char != pattern[pointer_to_pattern]:
                if char.isupper():
                    return False
        return pointer_to_pattern == len(pattern)

