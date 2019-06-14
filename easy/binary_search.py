class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = 0
        max_index = len(nums)
        
        while min_index <= max_index:
            middle_index = (min_index + max_index) // 2
            if middle_index == len(nums):
                break
            if nums[middle_index] == target:
                return middle_index
            if nums[middle_index] > target:
                max_index = middle_index - 1
            elif nums[middle_index] < target:
                min_index = middle_index + 1
        return -1
