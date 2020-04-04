class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2  # Gauss Formula
        return total - sum(nums)
