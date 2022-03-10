class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit,minPrice = 0,prices[0]
        
        for i in range(1,len(prices)):
            
            if prices[i] > minPrice:
                maxProfit = max(maxProfit,prices[i] - minPrice)
            else:
                minPrice = prices[i]
        
        return maxProfit
        
        