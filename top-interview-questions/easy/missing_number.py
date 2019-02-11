class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(1, len(nums) + 1):
            x += i
        for j in range(0, len(nums)):
            x -= nums[j]
        return x
