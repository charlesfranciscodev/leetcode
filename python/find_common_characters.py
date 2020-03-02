from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common_counter = Counter(A[0])
        for i in range(1, len(A)):
            counter = Counter(A[i])
            
            for letter, count in counter.items():
                if letter not in common_counter:
                    common_counter[letter] = 0
                elif common_counter[letter] > count:
                     common_counter[letter] = count
                        
            for letter, count in common_counter.items():
                if letter not in counter:
                    common_counter[letter] = 0
                elif counter[letter] < count:
                    common_counter[letter] = counter[letter]

        common_letters = []
        for letter, count in common_counter.items():
            for i in range(count):
                common_letters.append(letter)
        return common_letters
