class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        size = len(security)
        
        if time == 0:
            return range(size)
        
        goodDays=[]
        decreasing,increasing = 0,0
        
        for i in range(1,size-time):
            
            if security[i-1] >= security[i]:
                decreasing += 1 
            else:
                decreasing = 0
                
            if security[i+time-1] <= security[i+time]:
                increasing += 1 
            else:
                increasing = 0