class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]:
            return -1
        visited = set()
        directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        queue = deque([(0,0)])
        steps = 0
        rows, cols = len(grid),len(grid[0])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                visited.add((r,c))
                if (r,c) == (rows-1,cols-1):
                    return steps+1
                for dx,dy in directions:
                    if 0 <= r+dx < rows and 0 <= c+dy < cols:
                        if (r+dx,c+dy) not in visited and grid[r+dx][c+dy] == 0:
                            queue.append((r+dx,c+dy))
                            visited.add((r+dx,c+dy))
            steps += 1
        return -1