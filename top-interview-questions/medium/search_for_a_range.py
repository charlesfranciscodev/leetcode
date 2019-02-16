class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # binary search
        left = 0
        right = len(nums) - 1
        middle = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle
                right = middle
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        return [-1, -1]
