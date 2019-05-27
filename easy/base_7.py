class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = False
        if num < 0:
            num *= -1
            negative = True
        BASE = 7
        num_str = ""
        # avoid division by 0
        if (num == 0):
            num_str = '0'
            return num_str

        while (num != 0):
            num_str += str(num % BASE)  # remainder
            num //= BASE

        solution = num_str[::-1]
        if negative:
            solution = '-' + solution
            
        return solution
