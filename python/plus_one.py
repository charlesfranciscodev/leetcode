class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        exp = len(digits) - 1
        for digit in digits:
            num += digit * 10 ** exp
            exp -= 1
        num += 1
        
        return [int(x) for x in str(num)]
