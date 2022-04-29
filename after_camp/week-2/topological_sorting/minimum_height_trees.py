class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        inDegree = [0]*n
        
        for edge in edges:
            u,v = edge
            graph[u].add(v)
            graph[v].add(u)
            inDegree[u] += 1
            inDegree[v] += 1
            
        while len(graph) > 2:
            
            for vertices in graph:
                
                for neighbour in vertices:
                    
                    if inDegree[neighbour] == 1:
                        for neig in graph[neighbour]:
                            inDegree[neig] -= 1
                        graph[neighbour].remove()
                        
        return [key for key in graph.keys()]
                        

                