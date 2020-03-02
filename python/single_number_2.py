from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter()
        for n in nums:
            counter[n] += 1
        for n, count in counter.items():
            if count == 1:
                return n
