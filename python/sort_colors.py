class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = []
        for i in range(0, 3):
            counter.append(0)
        for i in range(0, len(nums)):
            counter[nums[i]] += 1
        i = 0
        j = 0
        while j < len(nums):
            while counter[i] == 0:
                i += 1
            nums[j] = i
            counter[i] -= 1
            j += 1
