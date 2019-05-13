class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_len = 0
        unique_chars = {}
        while i < len(s):
            c = s[i]
            if c in unique_chars:
                max_len = max(max_len, len(unique_chars))
                i = unique_chars[c] + 1
                unique_chars.clear()    
            else:
                unique_chars[c] = i
                i += 1
        max_len = max(max_len, len(unique_chars))
        return max_len
