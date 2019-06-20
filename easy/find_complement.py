class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit_count = len(bin(num)) - 2
        x = 2 ** (bit_count) - 1
        return num ^ x
