from collections import Counter


class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        uncommon_words = []
        
        words_a = a.split()
        words_b = b.split()
        
        words_a_set = set(words_a)
        words_b_set = set(words_b)
        
        words_a_counter = Counter(words_a)
        words_b_counter = Counter(words_b)
        
        words_to_delete = [word for word, count in words_a_counter.items() if count > 1]
        for word in words_to_delete:
            del words_a_counter[word]  
        words_to_delete = [word for word, count in words_b_counter.items() if count > 1]
        for word in words_to_delete:
            del words_b_counter[word]    
                
        for word in words_a_counter:
            if word not in words_b_set:
                uncommon_words.append(word)
        for word in words_b_counter:
            if word not in words_a_set:
                uncommon_words.append(word)

        return uncommon_words
