class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
         # top 3 positive values
        product1 = nums[-1] * nums[-2] * nums[-3]
        # bottom 2 values with top positive value
        product2 = nums[-1] * nums[0] * nums[1]
        return max(product1, product2)
