# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        previous_interval = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if self.checkOverlap(previous_interval, interval):
                count += 1
            else:
                previous_interval = interval
        return count

    def checkOverlap(self, interval1, interval2):
        x1, y1 = interval1
        x2, y2 = interval2
        ret = (y1 > x2 and y2 > x1) or (x1 == x2 and y1 == y2)
        return ret

