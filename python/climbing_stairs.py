class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        results = [0, 1, 2]
        
        i = 2
        while (i < n):
            next_result = results[i] + results[i - 1]
            results.append(next_result)
            i += 1
        
        return results[n]
