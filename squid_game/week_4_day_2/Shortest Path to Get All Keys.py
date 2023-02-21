class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        keys_count = 0
        start = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = (r,c)
                if 96 < ord(grid[r][c]) < 123:
                    keys_count += 1

        moves = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque([(*start,"")])
        visited = set()
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r,c,keys_found = queue.popleft()
                if len(keys_found) == keys_count:
                    return moves
                for dx,dy in directions:
                    if (0 <= r+dx < rows and 0 <= c+dy < cols and
                        grid[r+dx][c+dy] != "#" and
                        (r+dx,c+dy,keys_found) not in visited):
                        visited.add((r+dx,c+dy,keys_found))
                        if (64 < ord(grid[r+dx][c+dy]) < 91 and
                            grid[r+dx][c+dy].lower() not in keys_found):
                            continue
                        if (96 < ord(grid[r+dx][c+dy]) < 123 and 
                            grid[r+dx][c+dy] not in keys_found):
                            new_keys = keys_found + grid[r+dx][c+dy]
                            queue.append((r+dx,c+dy,new_keys))
                        else:
                            queue.append((r+dx,c+dy,keys_found))
                    
                
            moves += 1
            
        return -1