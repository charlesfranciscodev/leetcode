from collections import defaultdict

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """       
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        
        for c, count in counter.items():
            if (count == 1):
                return s.index(c)

        return -1
