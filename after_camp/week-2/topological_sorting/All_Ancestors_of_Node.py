class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
    
        graph = defaultdict(set)
        for u,v in edges:
            graph[v].add(u)
        
        def dfs(node):

            ancestors = set()
            visited.add(node)

            for neighbour in graph[node]:
                
                if neighbour not in visited:
                    ancestors |= dfs(neighbour)
                else:
                    ancestors |= allAncestors[neighbour]
                
                ancestors.add(neighbour)

            allAncestors[node] = ancestors

            return ancestors

        allAncestors = [0]*n
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                
        return [sorted(ancestors) for ancestors in allAncestors]