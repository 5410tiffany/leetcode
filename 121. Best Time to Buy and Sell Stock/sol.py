class Solution:
    def maxProfit(self, prices):
        
        mintili = inf
        profit = 0
        
        for i in range(len(prices)):
            
            # profit we will get assumes sell at day i
            profit = max(profit, prices[i] - mintili)
            
            # update the best timing to buy stocks
            mintili = min(mintili, prices[i])
            
        return profit
        
