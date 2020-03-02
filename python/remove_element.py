class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            x = nums[i]
            if x == val:
                nums.remove(x)
            else:
                i += 1
        return len(nums)
