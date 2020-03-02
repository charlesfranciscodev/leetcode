import math
import itertools


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        permutations = itertools.permutations(points)
        for permutation in permutations:
            if self.is_valid(permutation):
                return True
        return False

    def is_valid(self, points):
        p1, p2, p3, p4 = points
        
        d1 = self.distance(p1, p2)
        d2 = self.distance(p2, p3)
        d3 = self.distance(p3, p4)
        d4 = self.distance(p4, p1)

        a1 = self.angle(p1, p2, p3)
        a2 = self.angle(p2, p3, p4)
        a3 = self.angle(p3, p4, p1)
        a4 = self.angle(p4, p1, p2)
        
        return (d1 == d2 == d3 == d4) and (90 == a1 == a2 == a3 == a4)

    def distance(self, p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1]- p1[1])
    
    def angle(self, p1, p2, p3):
        angle = round(math.degrees(
            math.atan2(p3[1] - p2[1], p3[0] - p2[0]) - math.atan2(p1[1] - p2[1], p1[0] - p2[0])
        ))
        return angle + 360 if angle < 0 else angle
