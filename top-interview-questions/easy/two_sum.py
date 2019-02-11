class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if (other_num in num_dict):
                return [num_dict[other_num], i]
            if (num not in num_dict):
                num_dict[num] = i
