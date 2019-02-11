class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums2 = [0] * len(nums) 
        
        for i in range(0, len(nums)):
            j = (i + k) % len(nums) 
            nums2[j] = nums[i]
            
        for i in range(0, len(nums)):
            nums[i] = nums2[i]
