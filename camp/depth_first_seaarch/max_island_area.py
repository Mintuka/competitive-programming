class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            if grid[row][col] == 1:
                
                grid[row][col] = 0
                up,down,left,right = 0,0,0,0    
                
                if row > 0: up = dfs(row-1,col)
                if row < len(grid)-1: down = dfs(row+1,col)
                if col > 0: left = dfs(row,col-1)
                if col < len(grid[0])-1: right = dfs(row,col+1)
                
                maxArea = 1+up+down+left+right
                return maxArea
            
            else: return 0
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: maxArea = max(maxArea,dfs(i,j))
                    
        return maxArea