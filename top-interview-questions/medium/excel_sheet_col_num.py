class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        number = 0
        for char in s:
            number *= 26
            number += ord(char) - ord('A') + 1
        return number
