class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for num in nums:
            if (num in num_set):
                return True
            else:
                num_set.add(num)
        return False
