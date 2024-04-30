# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        ret = ''
        for i in range(n):
            ret += self.getWordIndexorEmptyString(word1, i)
            ret += self.getWordIndexorEmptyString(word2, i)
        return ret

    def getWordIndexorEmptyString(self, word, i):
        try:
            ret = word[i]
        except IndexError:
            ret = ''
        return ret

