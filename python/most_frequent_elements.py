# bucket sort solution

from collections import Counter

class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        counter = Counter()
        bucket = [None] * (len(nums) + 1)
        most_frequent = []
        
        for n in nums:
            counter[n] += 1
        
        for n, count in counter.items():
            if bucket[count] == None:
                bucket[count] = []
            bucket[count].append(n)
            
        for i in range(len(bucket) - 1, -1, -1):
            if len(most_frequent) == k:
                break
            
            if bucket[i] is not None:
                for n in bucket[i]:
                    if len(most_frequent) == k:
                        break
                    else:
                        most_frequent.append(n)

        return most_frequent
