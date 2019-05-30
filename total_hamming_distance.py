# https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for i in range(0, 32):
            count = 0
            for j in range(0, len(nums)):
                if nums[j] & (1 << i):
                    count += 1
            total += count * (len(nums) - count)
        return total
