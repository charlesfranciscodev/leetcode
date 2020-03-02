from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: 'List[str]') -> 'List[List[str]]':
        word_dict = defaultdict(list)
        for word in words:
            word_dict["".join(sorted(word))].append(word)
        return list(word_dict.values())
