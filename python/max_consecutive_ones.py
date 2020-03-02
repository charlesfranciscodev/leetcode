class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive_ones = consecutive_ones = 0
        for num in nums:
            if num == 1:
                consecutive_ones += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
                consecutive_ones = 0
        max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
        return max_consecutive_ones
