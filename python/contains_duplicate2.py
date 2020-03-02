from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = defaultdict(list)  # value => indexes in nums
        for i, num in enumerate(nums):
            if num in positions:
                for j in positions[num]:
                    if i - j <= k:
                        return True
                positions[num].append(i)
            else:
                positions[num].append(i)
        return False
