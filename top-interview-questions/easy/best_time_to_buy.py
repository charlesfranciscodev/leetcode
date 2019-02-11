class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        min_price = math.inf
        max_gain = 0
        
        for i in range(0, len(prices)):
            current_price = prices[i]
            if (current_price < min_price):
                min_price = current_price
            else:
                gain = current_price - min_price
                max_gain = max(max_gain, gain)
        
        return max_gain
