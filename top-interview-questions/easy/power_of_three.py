class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n >= 9):
            n /= 3
        return n == 3 or n == 1
