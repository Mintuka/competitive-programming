from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        leastTime,n = grid[0][0],len(grid)
        minHeap     = [(grid[0][0],0,0)]
        visited     = [[False for _ in range(len(grid))] for _ in range(len(grid))]
        
        while minHeap:
            popped = heappop(minHeap)
            time,row,col = popped
           
            if row == n-1 and col == n-1: return leastTime
            
            visited[row][col] = True
            
            if row > 0 and not visited[row-1][col]: 
                visited[row-1][col] = True
                heappush(minHeap,(grid[row-1][col],row-1,col))
            
            if col > 0 and not visited[row][col-1]: 
                visited[row][col-1] = True
                heappush(minHeap,(grid[row][col-1],row,col-1))
            
            if row < n-1 and not visited[row+1][col]: 
                visited[row+1][col] = True
                heappush(minHeap,(grid[row+1][col],row+1,col))
            
            if col < n-1 and not visited[row][col+1]: 
                visited[row][col+1] = True
                heappush(minHeap,(grid[row][col+1],row,col+1))
            
            if minHeap: leastTime = max(leastTime,minHeap[0][0])