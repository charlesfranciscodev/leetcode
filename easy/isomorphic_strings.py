class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        values = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                if c2 in values:
                    return False
                mapping[c1] = c2
                values.add(c2)
        return True
