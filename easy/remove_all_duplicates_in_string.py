class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = list(s)
        while True:
            contains_duplicate = False
            i = 0
            while i < len(a) - 1:
                if a[i] == a[i + 1]:
                    a.pop(i)
                    a.pop(i)
                    contains_duplicate = True
                i += 1
            if not contains_duplicate:
                break
        return ''.join(a)
