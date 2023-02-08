# https://leetcode.com/problems/valid-square/
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        lengths = sorted([
            self.getLengthSquare(p1, p2),
            self.getLengthSquare(p1, p3),
            self.getLengthSquare(p1, p4),
            self.getLengthSquare(p2, p3),
            self.getLengthSquare(p2, p4),
            self.getLengthSquare(p3, p4),
        ])
        return lengths[0] and lengths == [lengths[0], lengths[0], lengths[0], lengths[0], 2*lengths[0], 2*lengths[0]]
        
    def getLengthSquare(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return (x1 - x2)**2 + (y1 - y2)**2

