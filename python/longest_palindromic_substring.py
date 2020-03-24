class Solution:
    def is_palindrome(self, string):
        return string == string[::-1]
    
    def longestPalindrome(self, string: str) -> str:
        for len_substring in range(len(string), 1, -1):
            for start_index in range(0, len(string) - len_substring + 1):
                end_index = start_index + len_substring
                substring = string[start_index:end_index]
                if self.is_palindrome(substring):
                    return substring

        return string[0] if string else string
