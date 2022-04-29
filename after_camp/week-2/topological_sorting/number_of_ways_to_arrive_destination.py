class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for u,v,time in roads:
            graph[u].add((v,time))
            graph[v].add((u,time))
            
        minWays = [[inf,0]]*n
        minWays[0] = [0,1]
        minHeap = [(0,0)]
        
        while minHeap:
            
            time,node = heappop(minHeap)
                    
            for neighbour,newTime in graph[node]:
                
                if time + newTime < minWays[neighbour][0]:
                    minWays[neighbour] = [time + newTime,minWays[node][1]] 
                    heappush(minHeap,(time + newTime,neighbour))
                elif time + newTime == minWays[neighbour][0]:
                    minWays[neighbour][1] += minWays[node][1]
                    
        return minWays[-1][1]%1000000007