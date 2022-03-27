class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
        def dfs(i,j):
            if grid[i][j] == 1:
                grid[i][j] = 0
                if i > 0 and grid[i-1][j] == 1: dfs(i-1,j)
                if j > 0 and grid[i][j-1] == 1: dfs(i,j-1)
                if i < row-1 and grid[i+1][j] == 1: dfs(i+1,j)
                if j < col-1 and grid[i][j+1] == 1: dfs(i,j+1)

        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)
            
        for j in range(col):
            dfs(0,j)
            dfs(row-1,j)
            
        landCells = 0
        for i in range(row):
            for j in range(col): 
                if grid[i][j] == 1: landCells += 1
                    
        return landCells