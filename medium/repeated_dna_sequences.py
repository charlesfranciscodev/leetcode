class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        solution = set()
        sequences = set()
        limit = len(s) - 9
        for i in range(0, limit):
            sequence = s[i:i + 10]
            if sequence in sequences:
                solution.add(sequence)
                
            else:
                sequences.add(sequence)
        return list(solution)
