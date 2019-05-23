from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        if len(points) < 3:
            return total

        for point1 in points:
            counter = Counter()
            for point2 in points:
                distance = self.distance(point1, point2)
                counter[distance] += 1
            for count in counter.values():
                total += count * (count - 1)
                
        return total

    def distance(self, point1: List[int], point2: List[int]):
        return (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
