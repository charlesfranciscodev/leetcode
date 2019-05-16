import re


class Solution:
    def reverseWords(self, s: str) -> str:
        clean_str = re.sub(r" +", ' ', s).strip()
        words = clean_str.split()
        words.reverse()
        return ' '.join(words)
