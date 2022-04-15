from math import inf
from collections import defaultdict

def countPaths(n, roads):
    
    def dfs(node,visited):
        
        if node == n-1:
            return (0,1)
        
        visited[node] = [inf,inf]
        minTime       = [inf,inf]
        
        for u,time in graph[node]:
            
            if u not in visited:
                
                current = dfs(u,visited)
                
                if current[0]+time < minTime[0]:
                    minTime = [current[0]+time,current[1]]
                elif current[0]+time == minTime[0]:
                    minTime[1] += current[1]
            
            else:
            
                for nei in graph[u]:
                    if nei[0] != n-1 and visited[nei[0]][0] < visited[u][0]:
                        visited[u] = visited[nei]
                current = visited[u]
                
                if current[0]+time < minTime[0]:
                    minTime = [current[0]+time,current[1]]
                elif current[0]+time == minTime[0]:
                    minTime[1] += current[1]
                    
        visited[node] = minTime
                                
        return minTime
            
    graph = defaultdict(list)
    
    for u,v,time in roads:
        graph[u].append((v,time))
        graph[v].append((u,time))
        
    visited = defaultdict(list)
    
    return dfs(0,visited)[1]
n = 7 
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
countPaths(n,roads)

# from collections import defaultdict
# from collections import deque

# def gardenNoAdj(n, paths):
    
#     flowers = defaultdict(set)
#     graph = defaultdict(set)
#     visited = set()
    
#     for path in paths:
#         graph[path[0]].add(path[1])
#         graph[path[1]].add(path[0])
        
#     queue = deque([1])
#     visited.add(1)
#     while len(flowers) < n and queue:
        
#         flower = set([1,2,3,4])
#         garden = queue.popleft()
        
#         for neighbour in graph[garden]:
            
#             flower -= flowers[neighbour]
            
#             if neighbour not in visited:
#                 queue.append(neighbour)
#                 visited.add(neighbour)

#         flowers[garden].add(list(flower)[0])
        
#     return [flower for flower in flowers.values()]
        
# n = 4
# paths = [[1,2],[2,3],[3,1]]
# print(gardenNoAdj(n,paths))
