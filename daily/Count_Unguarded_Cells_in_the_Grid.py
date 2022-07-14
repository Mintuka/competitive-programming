class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        guards => 1, walls => 2, others => 0
        dfs over the grid if the cell is guard until you find a wall or guard
        convert zeros to 3 when discovered
        """
                    
        def dfs(r,c):

            #up
            for i in range(r-1,-1,-1):
                if grid[i][c] != 1 or grid[i][c] != 2:
                    grid[i][c] = 3
                else:
                    break
            #left
            for i in range(c-1,-1,-1):
                if grid[r][i] != 1 or grid[r][i] != 2:
                    grid[r][i] = 3
                else:
                    break
            #down
            for i in range(r+1,m):
                if grid[i][c] != 1 or grid[i][c] != 2:
                    grid[i][c] = 3
                else:
                    break
            #right
            for i in range(c+1,n):
                if grid[r][i] != 1 or grid[r][i] != 2:
                    grid[r][i] = 3
                else:
                    break
                
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for r,c in guards:
            grid[r][c] = 1
        for r,c in walls:
            grid[r][c] = 2
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)

                
        unguarded_cells = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_cells += 1
                    
        return unguarded_cells
            