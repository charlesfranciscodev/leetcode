class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        exponent = 0
        result = 4 ** exponent
        while result < num:
            exponent += 1
            result = 4 ** exponent
        return result == num
