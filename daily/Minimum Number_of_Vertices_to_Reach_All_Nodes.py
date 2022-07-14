class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        traverse the vertices in order from 0 to n-1
        continue if it is visited
        if not visited and has neighbours include it in the set
        if node in smallest_set is found as a neighbour of current node discard it from the set
        """
        
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
                if neighbour in smallest_set:
                    smallest_set.discard(neighbour)
        
        smallest_set = set()
        graph = defaultdict(set)
        visited = set()
        
        for _from,_to in edges:
            graph[_from].add(_to)
            
        for i in range(n):
            if len(graph[i]) and i not in visited:
                dfs(i)
                smallest_set.add(i)
                
        return smallest_set