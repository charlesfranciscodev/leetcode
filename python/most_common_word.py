import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        regex = r"\w+"
        words = re.findall(regex, paragraph)
        lowercase_words = map(str.lower, words)
        counter = Counter(lowercase_words)
        most_common_word, count = counter.most_common(1)[0]
        while most_common_word in banned_set:
            del counter[most_common_word]
            most_common_word, count = counter.most_common(1)[0]
        return most_common_word
