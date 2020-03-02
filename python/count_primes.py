class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(0, n):
            if (self.isPrime(i)):
                count += 1
        return count
        
    def isPrime(self, n):
        if (n <= 3):
            return n > 1
        elif (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6
        return True
