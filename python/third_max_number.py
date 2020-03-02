import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heapq._heapify_max(nums)
        if len(nums) >= 3:
            heapq._heappop_max(nums)
            heapq._heappop_max(nums)
        return nums[0]
