# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(self._permute(nums))

    def _permute(self, iterable):
        # https://github.com/python/cpython/blob/master/Modules/itertoolsmodule.c#L3213
        pool = tuple(iterable)
        n = len(pool)
        indices = list(range(n))
        cycles = list(range(n, 0, -1))
        yield tuple(pool[i] for i in indices[:n])
        while n:
            for i in reversed(range(n)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices)
                    break
            else:
                return

