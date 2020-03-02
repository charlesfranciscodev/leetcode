# https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        index = 0
        min_index = 0
        max_index = len(nums) - 1
        while min_index != max_index:
            index = (min_index + max_index) // 2
            print(index, min_index, max_index)
            if index % 2 == 0:
                if nums[index] == nums[index + 1]:
                    min_index = index + 2
                else:
                    max_index = index
            else:
                if nums[index] == nums[index - 1]:
                    min_index = index + 1
                else:
                    max_index = index - 1
        return nums[min_index]
