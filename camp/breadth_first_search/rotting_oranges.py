class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])     
                
        rottenList = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2: 
                    rottenList.append([i,j])
        
        totalTime = -1
        rotten = deque(rottenList)
        while rotten:
            size = len(rotten)
            for _ in range(size):
                i,j  = rotten.popleft()
                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rotten.append([i-1,j])
                if j > 0 and grid[i][j-1] == 1: 
                    grid[i][j-1] = 2
                    rotten.append([i,j-1])
                if i < row-1 and grid[i+1][j] == 1: 
                    grid[i+1][j] = 2
                    rotten.append([i+1,j])
                if j < col-1 and grid[i][j+1] == 1: 
                    grid[i][j+1] = 2
                    rotten.append([i,j+1])
            totalTime += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: return -1
                
        return totalTime if totalTime != -1 else 0