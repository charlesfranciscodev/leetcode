class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        if (negative):
            x *= -1
        
        s = str(x)
        reverse_x = 0
        for i in range(0, len(s)):
            digit = int(s[i])
            reverse_x += digit * 10 ** i
            
            
        if (negative):
            reverse_x *= -1
            if (reverse_x < -2 ** 31):
                return 0
        else:
            if (reverse_x > 2 ** 31 - 1):
                return 0
            
        return reverse_x
