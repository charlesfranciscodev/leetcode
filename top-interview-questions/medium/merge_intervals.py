# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from operator import attrgetter


class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []
        intervals.sort(key=attrgetter('start', 'end'))
        output = [intervals[0]]
        del intervals[0]
        for interval in intervals:
            prev_interval = output[-1]
            if self.lines_overlap(prev_interval.start, prev_interval.end, interval.start, interval.end):
                output[-1] = Interval(min(prev_interval.start, interval.start), max(prev_interval.end, interval.end))
            else:
                output.append(interval)
        return output
        
    def lines_overlap(self, x1, x2, x3, x4):
        return x2 >= x3 and x4 >= x1
