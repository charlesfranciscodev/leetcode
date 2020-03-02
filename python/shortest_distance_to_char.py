import math


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        shortest_distances = []
        for i, char in enumerate(s):
            if char == c:
                shortest_distances.append(0)
                continue
                
            left_distance = right_distance = math.inf
            
            left_index = s.rfind(c, 0, i)
            if left_index != -1:
                left_distance = i - left_index

            right_index = s.find(c, i, len(s))
            if right_index != -1:
                right_distance = right_index - i
            
            min_distance = min(left_distance, right_distance)
            shortest_distances.append(min_distance)
        return shortest_distances
