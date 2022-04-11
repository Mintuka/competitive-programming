class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        size = len(questions)
        dp   = [0]*size
        
        for i in range(size-1,-1,-1):
            
            points, brainPower = questions[i]
            
            pick,notPick = points,0
            
            if i + brainPower + 1 < size:
                pick += dp[i+brainPower+1]
                
            if i + 1 < size:
                notPick = dp[i+1]
                
            dp[i] = max(pick,notPick)
        
        return dp[0]