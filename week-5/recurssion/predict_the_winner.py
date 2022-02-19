class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[-1,-1] for i in range(n)] for i in range(n)]
        def winner(nums,i,j,p):
            if i > j:   return 0
            if dp[i][j][p] != -1: return dp[i][j][p]
            if p == 0:  
                dp[i][j][p] = max(nums[i]+winner(nums,i+1,j,1),nums[j]+winner(nums,i,j-1,1))
                return dp[i][j][p]
            else:       
                dp[i][j][p] = min(winner(nums,i+1,j,0),winner(nums,i,j-1,0))
                return dp[i][j][p]
        pOne = winner(nums,0,n-1,0)
        return pOne >= sum(nums) - pOne