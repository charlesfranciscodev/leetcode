class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        nums_set = set()
        for num in nums:
            if num in nums_set:
                duplicates.append(num)
            else:
                nums_set.add(num)
        return duplicates
