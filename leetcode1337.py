# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_rows = len(mat)
        num_soldiers_in_row = {}

        for i in range(num_rows):
            row = mat[i]
            soldiers_count = self.count_soldiers(row)
            num_soldiers_in_row[i] = soldiers_count

        after_sorted =  sorted(num_soldiers_in_row.items(), key=lambda x: x[1])
        rows_from_weak_to_strong = [i for i, soldiers_count in after_sorted]
        return rows_from_weak_to_strong[:k]

    def count_soldiers(self, row):
        count = 0
        for position in row:
            if position == 1:
                count += 1
        return count

