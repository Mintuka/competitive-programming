class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dp(row,col,memo):
            
            if memo[row][col] != -1: return memo[row][col]
            if row == len(triangle) - 1: return triangle[row][col]
            
            down    = dp(row+1,col,memo)
            diagonal= dp(row+1,col+1,memo)
            
            memo[row][col] = triangle[row][col] + min(down,diagonal)
            
            return memo[row][col]
        
        memo = [[-1 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        
        return dp(0,0,memo)
    
