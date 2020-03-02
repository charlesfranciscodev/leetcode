class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original_list = sorted(list(s))
        new_list = sorted(list(t))
        i = 0
        while i < len(original_list):
            if original_list[i] != new_list[i]:
                return new_list[i]
            i += 1
        return new_list[i]
