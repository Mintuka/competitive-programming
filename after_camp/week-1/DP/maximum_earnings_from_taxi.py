class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        size   = len(rides)
        rides  = sorted(rides, key=lambda x:x[0])
        starts = [rides[i][0] for i in range(size)]
        
        @lru_cache(None)
        def dp(i):
            
            if i >= size:
                
                return 0
                
            start,end,tip = 0,1,2
            
            pick = rides[i][end] - rides[i][start] + rides[i][tip]
            
           #find nextStart if the current is picked
                    # j = i + 1

                    # while j < size and rides[j][start] < rides[i][end]:
                    #      j += 1    
        
            j = bisect.bisect_left(starts,rides[i][end])

            pick += dp(j)
            notPick = dp(i+1)
            
            return max(pick,notPick)
    
        return dp(0)