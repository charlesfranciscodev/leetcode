import math

class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        x = y = math.inf
        for z in nums:
            if (z <= x):
                x = z
            elif (z <= y):
                y = z
            else:
                return True
        return False
