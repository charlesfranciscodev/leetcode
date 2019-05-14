class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        for len_sub_str in range(len(s), 0, -1):
            for i in range(0, len(s) - len_sub_str):
                end_index = i + len_sub_str
                sub_str = s[i:end_index + 1]
                
                if self.is_palindrome(sub_str):
                    return sub_str
        if len(s) > 0:
            return s[0]
        return s
