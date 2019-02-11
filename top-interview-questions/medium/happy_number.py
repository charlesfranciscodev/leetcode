class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        numbers = set()
        while (n != 1):
            string = str(n)
            n = 0
            for char in string:
                n += int(char) ** 2
            if (n in numbers):
                return False  # cycle
            else:
                numbers.add(n)
        return True
