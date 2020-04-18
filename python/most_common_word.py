import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.findall(r"\w+", paragraph)
        counter = Counter()
        for word in words:
            if word not in banned:
                counter[word] += 1
        return counter.most_common(1)[0][0]
