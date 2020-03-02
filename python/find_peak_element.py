class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        min_index = 0
        max_index = len(nums) - 1
        index = min_index + max_index // 2
        while index > -1 and index < len(nums):
            greater_than_right = index < len(nums) - 1 and nums[index] > nums[index + 1]
            greater_than_left = index > 0 and nums[index] > nums[index - 1]
            if greater_than_right and greater_than_left:
                break
            elif greater_than_right:
                if index == 0:
                    break
                max_index = index - 1
            else:
                if index == len(nums) - 1:
                    break
                min_index = index + 1
            index = (min_index + max_index) // 2
        return index
