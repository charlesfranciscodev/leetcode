class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s) // 2):
            temp = s[i]
            j  = len(s) - i - 1
            s[i] = s[j]
            s[j] = temp
