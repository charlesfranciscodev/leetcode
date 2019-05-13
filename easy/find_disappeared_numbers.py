class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        for i in range(1, len(nums) + 1):
            s.add(i)
        for x in nums: 
            s.discard(x)
        return list(s)
