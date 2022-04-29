from heapq import heappop,heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        size  = len(points)
        graph = defaultdict(list)
        
        for i in range(size):
            
            for j in range(size):
                
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                costOfNeighbour = (cost,tuple(points[j]))
                heappush(graph[tuple(points[i])],costOfNeighbour)
                    
        visited = set()
        visited.add(tuple(points[0]))
        minCost,size = 0,len(points)
        
        while len(visited) < size:
            
            findMin = [inf,(0,0),(0,0)]
            
            for node in visited:
                
                cost,vertice = graph[node][0]
                
                if cost < findMin[0] and vertice not in visited:
                    findMin = [cost,vertice,node]
                    
            
            graph[findMin[2]] and heappop(graph[findMin[2]])
            minCost += findMin[0]
            visited.add(findMin[1])
            
        return minCost