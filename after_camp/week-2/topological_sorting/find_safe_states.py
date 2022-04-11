class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        size     = len(graph)
        inDegree = [len(neighbours) for neighbours in graph]
        outgoing = defaultdict(set)
        queue    = deque()
        
        for i in range(size):
            
            if not graph[i]:
                queue.append(i)
            
            for node in graph[i]:
                outgoing[node].add(i)
                
        safeNodes = set()
        
        while queue:
            
            safe = queue.popleft()
            safeNodes.add(safe)
            
            for node in outgoing[safe]:
                inDegree[node] -= 1
                
                if inDegree[node] == 0:
                    queue.append(node)
                    
        return [i for i in range(size) if i in safeNodes]