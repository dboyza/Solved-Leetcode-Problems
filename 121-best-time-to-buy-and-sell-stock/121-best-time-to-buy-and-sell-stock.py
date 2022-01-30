class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """  
        max_profit = 0
        buy = prices[0]
        
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            max_profit = max(max_profit, prices[i] - buy)
            
        return max_profit
        
        