import math


class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        time_points_in_minutes = []
        for time_point in time_points:
            hours_minutes = time_point.split(':')
            hours = int(hours_minutes[0])
            minutes = int(hours_minutes[1])
            total_minutes = (hours * 60) + minutes
            time_points_in_minutes.append(total_minutes)
        time_points_in_minutes.sort()
        time_points_in_minutes.append((24 * 60) + time_points_in_minutes[0])
        min_difference = math.inf
        for i in range(0, len(time_points_in_minutes) - 1):
            difference = time_points_in_minutes[i + 1] - time_points_in_minutes[i]
            min_difference = min(min_difference, difference)
        return min_difference
