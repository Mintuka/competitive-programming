class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        size = len(prices)
        Periods,count = 0,0
        
        for i in range(1,size):
            
            if prices[i-1] - prices[i] == 1:
                
                count += 1
                
            else:
                
                count = 0
                
            if count:
                
                Periods = Periods + count
                
        return Periods + size