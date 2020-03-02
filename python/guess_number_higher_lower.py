# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_value = 1
        max_value = n
        guess_value = 1
        return_code = None
        while return_code != 0:
            guess_value = (min_value + max_value) / 2
            return_code = guess(guess_value)
            if return_code == -1:
                max_value = guess_value - 1
            elif return_code == 1:
                min_value = guess_value + 1
        return guess_value
