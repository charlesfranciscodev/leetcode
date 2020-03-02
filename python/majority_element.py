from collections import Counter

class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        counter = Counter()
        for num in nums:
            counter[num] += 1
        return counter.most_common(1)[0][0]
