class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        base = 0
        while base ** 2 < num:
            base += 1
        return base ** 2 == num
