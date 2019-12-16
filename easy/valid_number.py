class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            number = float(s)
            return True
        except ValueError:
            return False
