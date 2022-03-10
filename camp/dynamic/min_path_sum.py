from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = [[-1 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        
        def dp(row,col,memo):
            
            if memo[row][col] != -1: return memo[row][col]
            if row >= len(grid) or col >= len(grid[0]): return inf
            if row == len(grid)-1 and col == len(grid[0])-1: return grid[row][col]
            
            right = dp(row+1,col,memo) 
            down  = dp(row,col+1,memo)
            
            memo[row][col] = grid[row][col] + min(right,down)
            
            return memo[row][col]
        
        return dp(0,0,memo)